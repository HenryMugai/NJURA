"""
Authentication Service

Handles authentication and account-related
business logic for the N.J.U.R.A platform.
"""

from datetime import datetime

from werkzeug.security import (
    check_password_hash,
    generate_password_hash,
)

from database.db import db
from models import AuditLog, User


class AuthService:
    """
    Authentication service.
    """

    # =====================================================
    # User Lookup
    # =====================================================

    @staticmethod
    def get_by_id(user_id):
        """
        Returns a user by ID.
        """

        return User.query.filter_by(
            id=user_id,
            is_active=True,
            is_deleted=False
        ).first()

    @staticmethod
    def get_by_username(username):
        """
        Returns a user by username.
        """

        return User.query.filter_by(
            username=username,
            is_active=True,
            is_deleted=False
        ).first()

    @staticmethod
    def get_by_email(email):
        """
        Returns a user by email.
        """

        return User.query.filter_by(
            email=email,
            is_active=True,
            is_deleted=False
        ).first()

    # =====================================================
    # Password Utilities
    # =====================================================

    @staticmethod
    def hash_password(password):
        """
        Generates a secure password hash.
        """

        return generate_password_hash(password)

    @staticmethod
    def verify_password(password, password_hash):
        """
        Verifies a password against its hash.
        """

        return check_password_hash(
            password_hash,
            password
        )

    # =====================================================
    # Authentication
    # =====================================================

    @staticmethod
    def authenticate(username, password):
        """
        Authenticates a user.
        """

        user = AuthService.get_by_username(username)

        if not user:
            return None

        if user.account_status != "Active":
            return None

        if user.locked_until:

            if user.locked_until > datetime.utcnow():
                return None

        if not AuthService.verify_password(
            password,
            user.password_hash
        ):

            user.failed_login_attempts += 1

            if user.failed_login_attempts >= 5:

                from datetime import timedelta

                user.locked_until = (
                    datetime.utcnow()
                    + timedelta(minutes=30)
                )

            db.session.commit()

            return None

        user.failed_login_attempts = 0
        user.locked_until = None
        user.last_login_at = datetime.utcnow()

        db.session.commit()

        return user

    # =====================================================
    # Password Management
    # =====================================================

    @staticmethod
    def change_password(user, new_password):
        """
        Changes a user's password.
        """

        user.password_hash = AuthService.hash_password(
            new_password
        )

        user.password_changed_at = datetime.utcnow()

        user.force_password_change = False

        db.session.commit()

        return user

    @staticmethod
    def reset_password(user, password):
        """
        Resets a user's password.
        """

        user.password_hash = AuthService.hash_password(
            password
        )

        user.password_changed_at = datetime.utcnow()

        user.force_password_change = True

        db.session.commit()

        return user

    # =====================================================
    # Account Management
    # =====================================================

    @staticmethod
    def activate_user(user):
        """
        Activates a user account.
        """

        user.account_status = "Active"

        db.session.commit()

        return user

    @staticmethod
    def suspend_user(user):
        """
        Suspends a user account.
        """

        user.account_status = "Suspended"

        db.session.commit()

        return user

    @staticmethod
    def lock_user(user):
        """
        Locks a user account.
        """

        user.account_status = "Locked"

        db.session.commit()

        return user

    @staticmethod
    def unlock_user(user):
        """
        Unlocks a user account.
        """

        user.account_status = "Active"
        user.failed_login_attempts = 0
        user.locked_until = None

        db.session.commit()

        return user

    # =====================================================
    # Verification
    # =====================================================

    @staticmethod
    def verify_email(user):
        """
        Marks email as verified.
        """

        user.email_verified = True

        db.session.commit()

    @staticmethod
    def verify_phone(user):
        """
        Marks phone as verified.
        """

        user.phone_verified = True

        db.session.commit()

    # =====================================================
    # Audit Logging
    # =====================================================

    @staticmethod
    def create_audit_log(
        user,
        action,
        description,
        ip_address=None,
        user_agent=None
    ):
        """
        Creates an authentication audit log.
        """

        log = AuditLog(

            company_id=user.company_id,

            user_id=user.id,

            module="Authentication",

            action=action,

            description=description,

            entity_type="User",

            entity_id=user.id,

            ip_address=ip_address,

            user_agent=user_agent,

            status="Success"

        )

        db.session.add(log)
        db.session.commit()

        return log

    # =====================================================
    # Last Login
    # =====================================================

    @staticmethod
    def update_last_login(
        user,
        ip_address=None
    ):
        """
        Updates login information.
        """

        user.last_login_at = datetime.utcnow()

        if ip_address:

            user.last_login_ip = ip_address

        db.session.commit()

        return user