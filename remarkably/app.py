from flask import Flask
from flask_migrate import Migrate

from config import app_config
from db import db


def create_app(config_name):
    app = Flask(__name__)

    # Load config
    app.config.from_object(app_config[config_name])

    # Initialize database
    db.init_app(app)

    # Initialize migrations
    Migrate(app, db)

    return app
