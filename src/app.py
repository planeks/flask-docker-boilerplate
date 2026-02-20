import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config as configuration
from celery_app import init_celery

server = Flask(__name__)

config_name = os.environ.get("CONFIGURATION", "dev")
server.config.from_object(configuration.ENV_CONFIG_MAP[config_name])

db = SQLAlchemy()
db.init_app(server)
Migrate(server, db)

celery_app = init_celery(server)
server.extensions["celery"] = celery_app


if __name__ == "__main__":
    server.run(debug=True)  # noqa: S201
