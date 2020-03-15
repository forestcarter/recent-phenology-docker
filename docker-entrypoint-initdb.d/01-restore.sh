#!/bin/bash

file="/docker-entrypoint-initdb.d/dump.pgdata"

echo "Restoring DB using $file"

psql -U $POSTGRES_USER --dbname=$POSTGRES_DB -c "CREATE EXTENSION postgis;"
psql -U $POSTGRES_USER --dbname=$POSTGRES_DB -c "CREATE ROLE webclient with LOGIN PASSWORD '$WEBCLIENT_PW';"
psql -U $POSTGRES_USER --dbname=$POSTGRES_DB -c "CREATE ROLE $POSTGRES_USER  with LOGIN PASSWORD '$POSTGRES_PASSWORD';"
psql -U $POSTGRES_USER --dbname=$POSTGRES_DB -c "GRANT SELECT ON ALL TABLES IN SCHEMA public TO webclient;"
pg_restore -U postgres --dbname=$POSTGRES_DB --verbose --single-transaction < "$file" || exit 1


