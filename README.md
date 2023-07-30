Implementation

Backend: django restframework
Database: postgresql
Backend-server: gunicorn
Web-server: nginx (from docker image)
Frontend: react (was provided)
frontend available at: localhost:3000
backend at: localhost:8000

How to launch project locally using docker for every service

Project is set to start all necessary docker containers and populate database from single command.
Just perform the following command: docker-compose up --build -d

How to launch project locally using docker only for db and front

If for some reason you want to launch django manually:

Change DATABASES['HOST'] to 'localhost' in line 92 in django_backend/django_backend/settings.py
Perform the following commands in succession:
cd deploy
docker-compose up --build -d to start frontend and db cd ../backend_django
./manage.py migrate
./manage.py loadall
django-admin runserver to start backend
