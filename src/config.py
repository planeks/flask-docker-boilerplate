import logging
import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

PROJECT_NAME = 'MySet'

# It's important for this config file to be in the root of the project
APP_BASE_DIR = os.path.join(
    os.path.abspath(os.path.dirname(__file__))
)

ENV_CONFIG_MAP = {
    'dev': 'config.DevConfig',
    'test': 'config.TestConfig',
    'prod': 'config.ProdConfig'
}

class BaseConfig:
    SERVER_NAME = os.environ.get('SERVER_NAME')
    APPLICATION_ROOT = os.environ.get('APPLICATION_ROOT')
    PREFERRED_URL_SCHEME = os.environ.get('PREFERRED_URL_SCHEME')

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DEBUG = os.environ.get('FLASK_DEBUG', '0') == '1'
    TESTING = os.environ.get('TESTING', False) == 'True'

    LOGGER_NAME = "%s_log" % PROJECT_NAME
    LOG_LEVEL = logging.DEBUG

    PERMANENT_SESSION_LIFETIME = timedelta(days=7)

    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', 587))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'True') == 'True'
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = (os.environ.get('MAIL_DEFAULT_SENDER_NAME'),
                           os.environ.get('MAIL_DEFAULT_SENDER_EMAIL'))

    # CELERY
    CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL')
    CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND')
    CELERY_TASK_TRACK_STARTED = True
    CELERY_TASK_TIME_LIMIT = 30 * 60
    CELERY_TASK_SOFT_TIME_LIMIT = 25 * 60


class DevConfig(BaseConfig):
    SQLALCHEMY_RECORD_QUERIES = True
    MAIL_SUPPRESS_SEND = True


class TestConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.sqlite3'
    SQLALCHEMY_ECHO = False
    WTF_CSRF_ENABLED = False
    MAIL_SUPPRESS_SEND = True


class ProdConfig(BaseConfig):
    pass
