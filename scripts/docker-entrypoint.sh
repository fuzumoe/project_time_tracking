#!/bin/sh
set -e
echo "${DJANGO_SETTINGS_MODULE}"

if [ "${DJANGO_SETTINGS_MODULE}" = "project_time_tracking.settings.development" ]; then

until psql "postgresql://${SQL_USER}:${SQL_PASSWORD}@${SQL_HOST}/${SQL_DATABASE}" -c '\l'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 5
done

fi
#migrate
python /code/manage.py migrate --noinput

exec "$@"
