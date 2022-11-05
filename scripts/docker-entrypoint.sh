#!/bin/sh
set -e


until psql "postgresql://$SQL_USER:$SQL_PASSWORD@$SQL_HOST/$SQL_DATABASE" -c '\l'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 5
done
#migrate
python /code/manage.py migrate --noinput

exec "$@"
