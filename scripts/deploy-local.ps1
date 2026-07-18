$ErrorActionPreference = "Stop"

$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
$composeFile = Join-Path $repoRoot "infra\compose\compose.yaml"
$healthUrl = "http://127.0.0.1:8080/api/health/ready"

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

Write-Host "Deploying Mini Telemetry Platform locally..."
Write-Host "Compose file: $composeFile"

Invoke-DockerCompose @("build", "api", "simulator")

Write-Host "Starting database and broker..."
Invoke-DockerCompose @("up", "-d", "db", "broker")

Write-Host "Running database migrations..."
Invoke-DockerCompose @("run", "--rm", "api", "python", "-m", "alembic", "upgrade", "head")

Write-Host "Starting application stack..."
Invoke-DockerCompose @("up", "-d")

Write-Host "Checking health endpoint..."
for ($attempt = 1; $attempt -le 30; $attempt++) {
    try {
        $response = Invoke-RestMethod -Uri $healthUrl -TimeoutSec 3
        if ($response.status -eq "ready") {
            Write-Host "Deploy succeeded. API is ready through NGINX."
            Write-Host "Health URL: $healthUrl"
            exit 0
        }
    }
    catch {
        Start-Sleep -Seconds 2
    }
}

Write-Error "Deploy failed: health check did not become ready."
exit 1
