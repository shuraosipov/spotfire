### Setting up the Spotfire database (PostgreSQL)

Create docker image containing psql client and with SQL scripts for creating data base and tables in it:
```
docker build -t spotfire-database-worker-psql .
```

Get secrets from secrets manager:
```
DB_HOST=$(aws secretsmanager get-secret-value --secret-id rds_admin | jq --raw-output '.SecretString' | jq -r .host)
DBADMIN_NAME=$(aws secretsmanager get-secret-value --secret-id rds_admin | jq --raw-output '.SecretString' | jq -r .username)
DBADMIN_PASSWORD=$(aws secretsmanager get-secret-value --secret-id rds_admin | jq --raw-output '.SecretString' | jq -r .password)
SERVERDB_NAME=$(aws secretsmanager get-secret-value --secret-id rds_admin | jq --raw-output '.SecretString' | jq -r .spotfire_db)
SERVERDB_USER=$(aws secretsmanager get-secret-value --secret-id rds_admin | jq --raw-output '.SecretString' | jq -r .spotfire_db_user)
SERVERDB_PASSWORD=$(aws secretsmanager get-secret-value --secret-id rds_admin | jq --raw-output '.SecretString' | jq -r .spotfire_db_password)
```

Run docker container with provided secrets:

```
docker run --env DB_HOST=$DB_HOST --env DBADMIN_NAME=$DBADMIN_NAME --env DBADMIN_PASSWORD=$DBADMIN_PASSWORD --env SERVERDB_NAME=$SERVERDB_NAME --env SERVERDB_USER=$SERVERDB_USER --env SERVERDB_PASSWORD=$SERVERDB_PASSWORD spotfire-database-worker-psql
```

