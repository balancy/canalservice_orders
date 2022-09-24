#!/bin/sh

python manage.py migrate --no-input
python manage.py refresh_orders_in_db
python manage.py runserver 0.0.0.0:8000