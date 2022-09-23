#!/bin/sh

python manage.py migrate --no-input
python manage.py collectstatic --no-input
python manage.py refresh_orders
python manage.py runserver 0.0.0.0:8000