"""
Database Configuration

Initializes all Flask extensions used
throughout the N.J.U.R.A application.
"""

from flask_bcrypt import Bcrypt
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# =====================================================
# Extensions
# =====================================================

db = SQLAlchemy()

migrate = Migrate()

login_manager = LoginManager()

bcrypt = Bcrypt()

limiter = Limiter(
    key_func=get_remote_address
)

# =====================================================
# Initialization
# =====================================================

def init_db(app):
    """
    Initializes all extensions.
    """

    db.init_app(app)

    migrate.init_app(app, db)

    login_manager.init_app(app)

    bcrypt.init_app(app)

    limiter.init_app(app)

    with app.app_context():
        import models


# =====================================================
# Session Helpers
# =====================================================

def save(instance):

    db.session.add(instance)

    db.session.commit()


def save_all(instances):

    db.session.add_all(instances)

    db.session.commit()


def delete(instance):

    db.session.delete(instance)

    db.session.commit()


def commit():

    db.session.commit()


def rollback():

    db.session.rollback()


def flush():

    db.session.flush()


def refresh(instance):

    db.session.refresh(instance)


def close():

    db.session.close()


# =====================================================
# Health Check
# =====================================================

def database_connected():

    try:

        db.session.execute(
            db.text("SELECT 1")
        )

        return True

    except Exception:

        return False