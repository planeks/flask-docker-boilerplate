from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import config as configuration
from celery_app import init_celery

server = Flask(__name__)

server.config.from_object(configuration.DevConfig)

db = SQLAlchemy()
celery_app = init_celery(server)
server.extensions["celery"] = celery_app


if __name__ == '__main__':
    server.run(debug=True)
