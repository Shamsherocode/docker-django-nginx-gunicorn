#!/bin/sh

python manage.py migrate --no-input
python manage.py collectstatic --no-input


gunicorn angular_web_app.wsgi:application --bind 0.0.0.0:8000