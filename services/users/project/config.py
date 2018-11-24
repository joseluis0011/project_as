# services/users/project/config.py

import os # <-- nuevo

class BaseConfig:
    """Configuración base"""
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False # <-- nuevo
    SECRET_KEY='my_secret_key'


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') # <-- nuevo


class TestingConfig(BaseConfig):
    """Configuración de prueba"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL') # <-- nuevo

class ProductionConfig(BaseConfig):
    """Configuración de producción"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') # <-- nuevo
