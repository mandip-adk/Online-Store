#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate store 0009 --fake || true
python manage.py migrate store 0010 --fake || true
python manage.py migrate

if [ -n "$DJANGO_SUPERUSER_USERNAME" ]; then
    python manage.py createsuperuser --noinput || true
fi

