param(
    [string]$BackupPath
)

$ErrorActionPreference = "Stop"

$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
$backupDir = Join-Path $repoRoot "local-artifacts\backups"
$containerName = "compose-db-1"
$restoreDatabase = "telemetry_restore_verify_$((Get-Date).ToUniversalTime().ToString('yyyyMMddHHmmss'))"
$containerBackupPath = "/tmp/restore-verification.dump"
$restoreDatabaseCreated = $false

function Invoke-Docker {
    param(
        [Parameter(Mandatory = $true)]
        [string[]]$DockerArgs
    )

    docker @DockerArgs
    if ($LASTEXITCODE -ne 0) {
        throw "docker failed: $($DockerArgs -join ' ')"
    }
}

if (-not $BackupPath) {
    $latestBackup = Get-ChildItem -LiteralPath $backupDir -Filter "telemetry-*.dump" -File |
        Sort-Object LastWriteTime -Descending |
        Select-Object -First 1

    if (-not $latestBackup) {
        throw "No backup file found in $backupDir"
    }

    $BackupPath = $latestBackup.FullName
}

$resolvedBackupPath = (Resolve-Path -LiteralPath $BackupPath).Path
$backupFile = Get-Item -LiteralPath $resolvedBackupPath
if ($backupFile.Length -le 0) {
    throw "Backup file is empty: $resolvedBackupPath"
}

$isRunning = docker inspect $containerName --format "{{.State.Running}}" 2>$null
if ($LASTEXITCODE -ne 0 -or $isRunning -ne "true") {
    throw "Database container '$containerName' is not running."
}

try {
    Write-Host "Copying backup into $containerName..."
    Invoke-Docker @(
        "cp",
        $resolvedBackupPath,
        "${containerName}:${containerBackupPath}"
    )

    Write-Host "Creating isolated restore database: $restoreDatabase"
    Invoke-Docker @(
        "exec",
        $containerName,
        "createdb",
        "--username=telemetry",
        $restoreDatabase
    )
    $restoreDatabaseCreated = $true

    Write-Host "Restoring backup..."
    Invoke-Docker @(
        "exec",
        $containerName,
        "pg_restore",
        "--username=telemetry",
        "--dbname=$restoreDatabase",
        "--no-owner",
        "--no-privileges",
        "--exit-on-error",
        $containerBackupPath
    )

    $verificationQuery = @"
SELECT
    (SELECT version_num FROM alembic_version) AS migration,
    (SELECT COUNT(*) FROM devices) AS devices,
    (SELECT COUNT(*) FROM telemetry_readings) AS telemetry_readings;
"@

    $verificationResult = docker exec $containerName psql `
        --username=telemetry `
        --dbname=$restoreDatabase `
        --tuples-only `
        --no-align `
        --command=$verificationQuery

    if ($LASTEXITCODE -ne 0) {
        throw "Restore verification query failed."
    }

    $parts = $verificationResult.Trim().Split("|")
    if ($parts.Count -ne 3 -or [int]$parts[1] -le 0 -or [int]$parts[2] -le 0) {
        throw "Restored database did not contain the expected migration, device, and telemetry data."
    }

    Write-Host "Restore verified."
    Write-Host "Migration: $($parts[0])"
    Write-Host "Devices: $($parts[1])"
    Write-Host "Telemetry readings: $($parts[2])"
}
finally {
    if ($restoreDatabaseCreated) {
        Write-Host "Removing isolated restore database..."
        docker exec $containerName dropdb `
            --username=telemetry `
            --if-exists `
            $restoreDatabase 2>$null
    }

    docker exec $containerName rm -f $containerBackupPath 2>$null
}
