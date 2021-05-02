import os

from app.utils.singleton import SingletonMeta


class Settings(metaclass=SingletonMeta):

    BASE_URL_DATA = 'https://1cc2f142-f451-4476-923b-c7a0ffca90c9.mock.pstmn.io'
    DATABASE_HOST = os.getenv("DATABASE_HOST")
    DATABASE_PORT = os.getenv("DATABASE_PORT")
    DATABASE_USER = os.getenv("DATABASE_USER")
    DATABASE_PASS = os.getenv("DATABASE_PASS")
    DATABASE_NAME = os.getenv("DATABASE_NAME")
    REDIS_HOSTNAME = os.getenv("REDIS_HOSTNAME")
    REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")
    MODELS_TORTOISE = ["app.models.client", 'app.models.client_proposal']

    def __init__(self):
        self.validate_database_host()
        self.validate_database_port()
        self.validate_database_user()
        self.validate_database_pass()
        self.validate_database_name()

    def validate_database_host(self):
        if self.DATABASE_HOST is None:
            raise ValueError("DATABASE_HOST should be not empty")

    def validate_database_port(self):
        if self.DATABASE_PORT is None:
            raise ValueError("DATABASE_PORT should be not empty")

    def validate_database_user(self):
        if self.DATABASE_USER is None:
            raise ValueError("DATABASE_USER should be not empty")

    def validate_database_pass(self):
        if self.DATABASE_PASS is None:
            raise ValueError("DATABASE_PASS should be not empty")

    def validate_database_name(self):
        if self.DATABASE_NAME is None:
            raise ValueError("DATABASE_NAME should be not empty")

