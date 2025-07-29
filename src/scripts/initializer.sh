#!/bin/bash

./src/scripts/wait-for-it.sh db:5432 --timeout=80 --strict -- echo "db is ready."

python src/manage.py collectstatic --noinput
python src/manage.py makemigrations
python src/manage.py migrate
# python manage.py runserver 0.0.0.0:8000

./src/scripts/tailwindcss.sh
