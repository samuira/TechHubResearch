#!/bin/sh
pwd
cd kpi
pwd
pip install -e . 
KPI migrate -o True
cd ..
pwd
# python manage.py makemigrations
#python manage.py migrate
#python manage.py collectstatic --noinput
# /usr/local/bin/gunicorn WorkForce.wsgi:application -w 2 -b :8000
exec "$@"