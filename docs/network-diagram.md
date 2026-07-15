# Network Diagram

```text
Host browser / tools
  | HTTP localhost:8001
  v
api service: mini-telemetry-api
  | HTTP inside container: 0.0.0.0:8000
  | PostgreSQL connection: db:5432
  v
db service: mini-telemetry-db
  | stores data at /var/lib/postgresql/data
  v
Docker named volume: compose_postgres_data
```

## Ports

| Service | Container port | Host port | Purpose |
|---|---:|---:|---|
| api | 8000 | 8001 | FastAPI HTTP |
| db | 5432 | 5433 | PostgreSQL local access |

## Startup Order

1. Compose starts `db`.
2. Docker runs `pg_isready` until `db` is healthy.
3. Compose starts `api`.
4. Docker checks `api` by calling `/health/ready` inside the API container.

`depends_on` controls startup order only. The application still needs readiness checks because a started process is not always ready to serve traffic.
