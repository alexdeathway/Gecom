#!/bin/sh

python manage.py loaddata db.json
python manage.py migrate --no-input
python manage.py collectstatic --no-input

gunicorn archiver.wsgi:application --bind 0.0.0.0:8000
