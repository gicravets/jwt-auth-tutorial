# project/server/config.py

import os
basedir = os.path.abspath(os.path.dirname(__file__))

pg_user = "user_flask_jwt_auth"
pg_pwd = "1q3e5t7u!!"
pg_port = "5432"

#postgres_local_base = 'postgresql://postgres:@localhost/'
postgres_local_base = 'postgresql://{username}:{password}@localhost:{port}/'.format(username=pg_user, password=pg_pwd, port=pg_port)
database_name = 'flask_jwt_auth'


class BaseConfig:
    """Base configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious')
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = postgres_local_base + database_name


class TestingConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = postgres_local_base + database_name + '_test'
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(BaseConfig):
    """Production configuration."""
    SECRET_KEY = 'my_precious'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql:///example'
