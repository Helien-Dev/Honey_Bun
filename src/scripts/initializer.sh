#!/bin/bash

./scripts/wait-for-it.sh db:5432 --timeout=80 --strict -- echo "db is ready."

python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000