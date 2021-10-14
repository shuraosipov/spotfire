Run Spotfire Server version 10.10.4 and Spotfire Database (Postgres 10.5) using docker-compose.
Database data will be stored locally under postgres-data directory, so your changes will survive docker-compose restarts.

### Important
This docker compose has hardcoded secrets. Use it carefully.

### Prerequisites
1. Spotfire Server installation files (tss-10.10.4.x86_64.rpm)
2. Postgres JDBC driver (postgresql-42.2.24.jar)


### Start
```
docker-compose up
```

### Stop
```
docker-compose down
```

### Access Spotfire
Spotfire Server will start on port 82. You can access it using the following URL:
```
http://localhost:82/spotfire
```

### Credentials
Username: admin
Password: spotfire

### Known issues
You might need to restart docker compose (docker-compose down / docker-compose up) during initial launch, as Spotfire Server might not connect to the database right away.