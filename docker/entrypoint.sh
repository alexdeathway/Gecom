#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

postgres_ready() {
    python << END
import sys

from psycopg2 import connect
from psycopg2.errors import OperationalError

try:
    connect(
        dbname="${POSTGRES_DATABASE}",
        user="${POSTGRES_USER}",
        password="${POSTGRES_PASSWORD}",
        host="${POSTGRES_HOST}",
        port="${POSTGRES_PORT}",
    )
except OperationalError:
    sys.exit(-1)
END
}

until postgres_ready; do
  >&2 echo "Waiting for PostgreSQL to become available..."
  sleep 5
done
>&2 echo "PostgreSQL is available"



if [ "$RUN_COLLECTSTATIC" = "True" ]; then
    echo "Running collectstatic"
    python3 manage.py collectstatic --noinput
else
    echo "Skipping collectstatic"
fi
python3 manage.py makemigrations
python3 manage.py migrate
python manage.py loaddata --exclude auth.permission --exclude contenttypes back.json
exec "$@"
