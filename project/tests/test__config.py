# project/tests/test_config.py


import unittest

from flask import current_app
from flask_testing import TestCase

from project.server import app

pg_user = "user_flask_jwt_auth"
pg_pwd = "1q3e5t7u!!"
pg_port = "5432"

class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object('project.server.config.DevelopmentConfig')
        return app

    def test_app_is_development(self):
        self.assertFalse(app.config['SECRET_KEY'] is 'my_precious')
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)
        self.assertTrue(
#           app.config['SQLALCHEMY_DATABASE_URI'] == 'postgresql://postgres:@localhost/flask_jwt_auth'
            app.config['SQLALCHEMY_DATABASE_URI'] == 'postgresql://{username}:{password}@localhost:{port}/flask_jwt_auth'.format(username=pg_user, password=pg_pwd, port=pg_port)
        )


class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object('project.server.config.TestingConfig')
        return app

    def test_app_is_testing(self):
        self.assertFalse(app.config['SECRET_KEY'] is 'my_precious')
        self.assertTrue(app.config['DEBUG'])
        self.assertTrue(
#           app.config['SQLALCHEMY_DATABASE_URI'] == 'postgresql://postgres:@localhost/flask_jwt_auth_test'
            app.config['SQLALCHEMY_DATABASE_URI'] == 'postgresql://{username}:{password}@localhost:{port}/flask_jwt_auth_test'.format(username=pg_user, password=pg_pwd, port=pg_port)
        )


class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object('project.server.config.ProductionConfig')
        return app

    def test_app_is_production(self):
        self.assertTrue(app.config['DEBUG'] is False)


if __name__ == '__main__':
    unittest.main()
