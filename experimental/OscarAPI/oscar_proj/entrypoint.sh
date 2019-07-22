#!/bin/sh
export JAM_AUTH_TOKEN='30000000000000889|155f5b95-a40a-4ae5-8273-41ae83fec8c9'
python manage.py makemigrations
python manage.py migrate
/usr/local/bin/gunicorn oscar_proj.wsgi:application -w 2 -b :8082
exec "$@"