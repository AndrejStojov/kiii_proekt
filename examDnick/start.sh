#!/bin/sh
echo "Collect static files"
python manage.py collectstatic --noinput
echo "Make migrations"
python manage.py makemigrations --no-input
python manage.py migrate --no-input
echo "Create superuser"
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'password')
EOF
python manage.py runserver 0.0.0.0:8000
exec "$@"
