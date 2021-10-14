Run Spotfire Server and Spotfire Library Database (Postgres) using docker-compose.

### Prerequisites
1. Spotfire Server installation files (10.10.4)
2. Postgres JDBC driver (e.g. postgresql-42.2.24.jar)


### Important
This docker compose is not secure. It contains secrets hardcoded in it.

### Lauch
```
docker-compose up
```

Spotfire will start on port 82.
