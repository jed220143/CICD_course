param(
    [string]$ImageTag = "v0.2.0"
)

$ErrorActionPreference = "Stop"

$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
$composeFile = Join-Path $repoRoot "infra\compose\compose.registry.yaml"
$healthUrl = "http://127.0.0.1:8080/api/health/ready"
$env:IMAGE_TAG = $ImageTag

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

Write-Host "Deploying from GHCR locally..."
Write-Host "Compose file: $composeFile"
Write-Host "Image tag: $ImageTag"

Write-Host "Pulling release images..."
Invoke-DockerCompose @("pull", "api", "simulator")

Write-Host "Starting database and broker..."
Invoke-DockerCompose @("up", "-d", "db", "broker")

Write-Host "Running database migrations from release image..."
Invoke-DockerCompose @("run", "--rm", "api", "python", "-m", "alembic", "upgrade", "head")

Write-Host "Starting application stack from release images..."
Invoke-DockerCompose @("up", "-d")

Test-Health
Write-Host "Registry deploy succeeded."
