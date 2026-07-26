#!/usr/bin/env bash
set -Eeuo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd -- "${SCRIPT_DIR}/.." && pwd)"
COMPOSE_FILE="${REPO_ROOT}/infra/compose/compose.yaml"
ENV_FILE="${REPO_ROOT}/infra/compose/.env.aws"
HEALTH_URL="http://127.0.0.1:8080/api/health/ready"
export IMAGE_TAG="${1:-v0.2.0}"

if [[ ! -f "${ENV_FILE}" ]]; then
  echo "Missing ${ENV_FILE}" >&2
  echo "Copy aws.env.example to .env.aws and set POSTGRES_PASSWORD." >&2
  exit 1
fi

if [[ "$(stat -c '%a' "${ENV_FILE}")" != "600" ]]; then
  echo "${ENV_FILE} must have permission 600." >&2
  echo "Run: chmod 600 ${ENV_FILE}" >&2
  exit 1
fi

compose() {
  docker compose --env-file "${ENV_FILE}" -f "${COMPOSE_FILE}" "$@"
}

echo "Validating AWS Compose configuration..."
compose config --quiet

echo "Pulling release images for ${IMAGE_TAG}..."
compose pull

echo "Starting PostgreSQL and MQTT broker..."
compose up -d db broker

echo "Running database migrations..."
compose run --rm api python -m alembic upgrade head

echo "Starting the application stack..."
compose up -d

echo "Waiting for readiness through NGINX..."
for attempt in $(seq 1 30); do
  if curl --fail --silent --show-error "${HEALTH_URL}" >/dev/null; then
    echo "Deploy succeeded: ${HEALTH_URL}"
    compose ps
    exit 0
  fi
  sleep 2
done

echo "Health check failed." >&2
compose ps >&2
exit 1
