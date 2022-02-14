#!/bin/sh


# systemctl start gunicorn.socket
# systemctl enable gunicorn.socket

python manage.py migrate --no-input
python manage.py collectstatic --no-input


gunicorn auth.wsgi:application --bind 0.0.0.0:8000