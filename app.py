from flask import Flask

from config import Config

from database.db import db
from database.db import migrate
from database.db import login_manager
from database.db import bcrypt
from database.db import limiter


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    # --------------------------------
    # Initialize Extensions
    # --------------------------------

    db.init_app(app)

    migrate.init_app(app, db)

    login_manager.init_app(app)

    bcrypt.init_app(app)

    limiter.init_app(app)

    # --------------------------------
    # Register Blueprints
    # --------------------------------

    # Added as we build each module.

    return app