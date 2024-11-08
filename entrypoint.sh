#!/bin/bash
cd Task

python manage.py makemigrations
python manage.py migrate
python manage.py load_currency

echo "from django.contrib.auth.models import User; User.objects.filter(email='admin@example.com').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'password123')" | python manage.py shell

python manage.py runserver 0.0.0.0:8000