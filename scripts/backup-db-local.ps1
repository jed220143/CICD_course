param(
    [ValidateRange(1, 365)]
    [int]$RetentionDays = 7
)

$ErrorActionPreference = "Stop"

$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
$backupDir = Join-Path $repoRoot "local-artifacts\backups"
$timestamp = (Get-Date).ToUniversalTime().ToString("yyyyMMdd-HHmmss")
$backupName = "telemetry-$timestamp.dump"
$backupPath = Join-Path $backupDir $backupName
$containerName = "compose-db-1"
$containerBackupPath = "/tmp/$backupName"

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

$isRunning = docker inspect $containerName --format "{{.State.Running}}" 2>$null
if ($LASTEXITCODE -ne 0 -or $isRunning -ne "true") {
    throw "Database container '$containerName' is not running."
}

New-Item -ItemType Directory -Force -Path $backupDir | Out-Null

try {
    Write-Host "Creating PostgreSQL backup inside $containerName..."
    Invoke-Docker @(
        "exec",
        $containerName,
        "pg_dump",
        "--username=telemetry",
        "--dbname=telemetry",
        "--format=custom",
        "--file=$containerBackupPath"
    )

    Write-Host "Validating backup catalog..."
    Invoke-Docker @(
        "exec",
        $containerName,
        "pg_restore",
        "--list",
        $containerBackupPath
    )

    Write-Host "Copying backup to host..."
    Invoke-Docker @(
        "cp",
        "${containerName}:${containerBackupPath}",
        $backupPath
    )

    $backupFile = Get-Item -LiteralPath $backupPath
    if ($backupFile.Length -le 0) {
        throw "Backup file is empty: $backupPath"
    }

    $hash = (Get-FileHash -LiteralPath $backupPath -Algorithm SHA256).Hash
    Write-Host "Backup verified."
    Write-Host "Path: $backupPath"
    Write-Host "Size: $($backupFile.Length) bytes"
    Write-Host "SHA256: $hash"

    $retentionCutoff = (Get-Date).AddDays(-$RetentionDays)
    Get-ChildItem -LiteralPath $backupDir -Filter "telemetry-*.dump" -File |
        Where-Object LastWriteTime -lt $retentionCutoff |
        Remove-Item -Force

    Write-Host "Retention: kept backups from the last $RetentionDays days."
}
finally {
    docker exec $containerName rm -f $containerBackupPath 2>$null
}
