### Implementation

1. Backend: django restframework
2. Database: postgresql
3. Backend-server: gunicorn
4. Web-server: nginx (from docker image)
5. Frontend: react (was provided)
6. frontend available at: localhost:3000
7. backend at: localhost:8000

### How to launch project locally using docker for every service

Project is set to start all necessary docker containers and populate database from single command.
Just perform the following command: `docker-compose up --build -d`

### How to launch project locally using docker only for db and front

If for some reason you want to launch django manually:

Change DATABASES['HOST'] to 'localhost' in line 92 in django_backend/django_backend/settings.py
Perform the following commands in succession:
1. `cd deploy`
2. `docker-compose up --build -d to start frontend and db cd ../backend_django`
3. `./manage.py migrate`
4. `./manage.py loadall`
5. `django-admin runserver to start backend`
