# Flask JWT Auth

[![Build Status](https://travis-ci.org/realpython/flask-jwt-auth.svg?branch=master)](https://travis-ci.org/realpython/flask-jwt-auth)

## Want to learn how to build this project?

Check out the [blog post](https://realpython.com/blog/python/token-based-authentication-with-flask/).

## Want to use this project?

### Basics

1. Fork/Clone
1. Activate a virtualenv
1. Install the requirements

### Set Environment Variables

user_flask_jwt_auth
flask_jwt_auth
lask_jwt_auth_test

```sh
sudo apt install postgresql postgresql-contrib -y
ss -nlt | grep 5432
sudo -u postgres psql -c "SELECT version();"
```

```sh
sudo su - postgres -c "createuser user_flask_jwt_auth;"
sudo su - postgres -c "alter user user_flask_jwt_auth with encrypted password '<password>';"
sudo su - postgres -c "createdb flask_jwt_auth;"
sudo su - postgres -c "createdb flask_jwt_auth_test;"
sudo su - postgres -c "grant all privileges on database flask_jwt_auth to user_flask_jwt_auth;"
sudo su - postgres -c "grant all privileges on database flask_jwt_auth_test to user_flask_jwt_auth;"
```

```sh
sudo su - postgres -c "create database <dbname>;"
sudo su - postgres -c "create user <username> with encrypted password '<password>';"
sudo su - postgres -c "grant all privileges on database <dbname> to <username>;"
```

```sh
pip install pyjwt==1.4.2
pip install psycopg2==2.9.3  
pip install psycopg2-binary==2.9.3
pip install --upgrade sqlalchemy
```

Update *project/server/config.py*, and then run:

```sh
$ export APP_SETTINGS="project.server.config.DevelopmentConfig"
```

or

```sh
$ export APP_SETTINGS="project.server.config.ProductionConfig"
```

Set a SECRET_KEY:

```sh
$ export SECRET_KEY="change_me"
```

### Create DB

Create the databases in `psql`:

```sh
$ psql
# create database flask_jwt_auth
# create database flask_jwt_auth_test
# \q
```

Create the tables and run the migrations:

```sh
$ python manage.py create_db
$ python manage.py db init
$ python manage.py db migrate
```

### Run the Application

```sh
$ python manage.py runserver
```

Access the application at the address [http://localhost:5000/](http://localhost:5000/)

> Want to specify a different port?

> ```sh
> $ python manage.py runserver -h 0.0.0.0 -p 8080
> ```

### Testing

Without coverage:

```sh
$ python manage.py test
```

With coverage:

```sh
$ python manage.py cov
```
# jwt-auth-tutorial
