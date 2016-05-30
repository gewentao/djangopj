python manage.py makemigrations
python manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('$ADMIN_USER_NAME', 'sailbear@foxmail.com', '$ADMIN_USER_PASSWORD')" | python manage.py shell
python manage.py runserver 0.0.0.0:80
