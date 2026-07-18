$ErrorActionPreference = "Stop"

$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
$composeFile = Join-Path $repoRoot "infra\compose\compose.yaml"
$healthUrl = "http://127.0.0.1:8080/api/health/ready"
$apiImage = "mini-telemetry-api:dev"
$simulatorImage = "mini-telemetry-simulator:dev"
$apiRollbackImage = "mini-telemetry-api:rollback"
$simulatorRollbackImage = "mini-telemetry-simulator:rollback"

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

function Invoke-DockerCompose {
    param(
        [Parameter(Mandatory = $true)]
        [string[]]$ComposeArgs
    )

    docker compose -f $composeFile @ComposeArgs
    if ($LASTEXITCODE -ne 0) {
        throw "docker compose failed: $($ComposeArgs -join ' ')"
    }
}

function Test-DockerImage {
    param(
        [Parameter(Mandatory = $true)]
        [string]$ImageName
    )

    docker image inspect $ImageName *> $null
    return $LASTEXITCODE -eq 0
}

function Save-RollbackImages {
    if (Test-DockerImage $apiImage) {
        Write-Host "Saving rollback image: $apiRollbackImage"
        Invoke-Docker @("tag", $apiImage, $apiRollbackImage)
    }

    if (Test-DockerImage $simulatorImage) {
        Write-Host "Saving rollback image: $simulatorRollbackImage"
        Invoke-Docker @("tag", $simulatorImage, $simulatorRollbackImage)
    }
}

function Test-Health {
    Write-Host "Checking health endpoint..."
    for ($attempt = 1; $attempt -le 30; $attempt++) {
        try {
            $response = Invoke-RestMethod -Uri $healthUrl -TimeoutSec 3
            if ($response.status -eq "ready") {
                Write-Host "API is ready through NGINX."
                Write-Host "Health URL: $healthUrl"
                return
            }
        }
        catch {
            Start-Sleep -Seconds 2
        }
    }

    throw "health check did not become ready"
}

function Restore-RollbackImages {
    $hasApiRollback = Test-DockerImage $apiRollbackImage
    $hasSimulatorRollback = Test-DockerImage $simulatorRollbackImage

    if (-not $hasApiRollback -and -not $hasSimulatorRollback) {
        Write-Warning "No rollback images are available."
        return
    }

    if ($hasApiRollback) {
        Write-Host "Restoring rollback image: $apiImage"
        Invoke-Docker @("tag", $apiRollbackImage, $apiImage)
    }

    if ($hasSimulatorRollback) {
        Write-Host "Restoring rollback image: $simulatorImage"
        Invoke-Docker @("tag", $simulatorRollbackImage, $simulatorImage)
    }

    Write-Host "Restarting stack with rollback images..."
    Invoke-DockerCompose @("up", "-d", "api", "simulator", "nginx")
    Test-Health
}

try {
    Write-Host "Deploying Mini Telemetry Platform locally..."
    Write-Host "Compose file: $composeFile"

    Save-RollbackImages

    Invoke-DockerCompose @("build", "api", "simulator")

    Write-Host "Starting database and broker..."
    Invoke-DockerCompose @("up", "-d", "db", "broker")

    Write-Host "Running database migrations..."
    Invoke-DockerCompose @("run", "--rm", "api", "python", "-m", "alembic", "upgrade", "head")

    Write-Host "Starting application stack..."
    Invoke-DockerCompose @("up", "-d")

    Test-Health
    Write-Host "Deploy succeeded."
    exit 0
}
catch {
    Write-Warning "Deploy failed: $($_.Exception.Message)"
    Write-Warning "Attempting application image rollback. Database schema is not downgraded automatically."

    try {
        Restore-RollbackImages
        Write-Warning "Rollback completed, but the new deploy failed. Check logs before retrying."
    }
    catch {
        Write-Error "Rollback failed: $($_.Exception.Message)"
    }

    exit 1
}
