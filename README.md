Installation
============
Run the following command to in a python 3 virtual environment, this will setup everything and start the server.
You can look at the `Makefile` to go deeper.
```commandline
make start_dev_server
```
This will setup everything ans start the server at `http://localhost:8000`

API Documentation
=================

1. To create an account `/api/register`
```commandline
curl --location --request POST 'http://127.0.0.1:8000/api/register' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email": "test@example.com",
    "username": "test",
    "password": "test123"
}'
```
2. To get the auth token `/api/login`
```commandline
curl --location --request POST 'http://127.0.0.1:8000/api/login' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "test",
    "password": "test123"
}'
```
3. Shortify the URL `/shortify`
```commandline
curl --location --request POST 'http://127.0.0.1:8000/shortify' \
--header 'Content-Type: application/json' \
--header 'Authorization: Token <replace-me-with-token>' \
--data-raw '{
    "url": "https://www.highsnobiety.com/p/louis-vuitton-basketball-sneakers/"
}'
```
4. User CRUD API `/api/user`
```commandline
curl --location --request GET 'http://127.0.0.1:8000/api/user' \
--header 'Content-Type: application/json' \
--header 'Authorization: Token <replace-me-with-token>'
```
__Note__: To make the user admin, you will have to login to admin portal `/admin` and assign a group named `admin` to the user.
Run this command to create a superuser for login in admin.
```commandline
python manage.py createsuperuser
```
# python-assignment
