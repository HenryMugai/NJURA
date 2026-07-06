from database.db import db
from models.base import BaseModel


class User(BaseModel):
    """
    Represents a system user.

    Handles authentication, authorization and
    account management for all users in N.J.U.R.A.
    """

    __tablename__ = "users"

    __table_args__ = (
        db.UniqueConstraint(
            "company_id",
            "username",
            name="uq_company_username"
        ),
    )

    # =====================================================
    # Foreign Keys
    # =====================================================

    company_id = db.Column(
        db.Integer,
        db.ForeignKey("companies.id"),
        nullable=True,
        index=True
    )

    role_id = db.Column(
        db.Integer,
        db.ForeignKey("roles.id"),
        nullable=False,
        index=True
    )

    # =====================================================
    # Basic Information
    # =====================================================

    first_name = db.Column(
        db.String(100),
        nullable=False
    )

    middle_name = db.Column(
        db.String(100),
        nullable=True
    )

    last_name = db.Column(
        db.String(100),
        nullable=False
    )

    username = db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(120),
        nullable=False,
        unique=True,
        index=True
    )

    phone = db.Column(
        db.String(20),
        nullable=True
    )

    profile_photo = db.Column(
        db.String(255),
        nullable=True
    )

    # =====================================================
    # Authentication
    # =====================================================

    password_hash = db.Column(
        db.String(255),
        nullable=False
    )

    password_changed_at = db.Column(
        db.DateTime,
        nullable=True
    )

    last_login_at = db.Column(
        db.DateTime,
        nullable=True
    )

    last_login_ip = db.Column(
        db.String(50),
        nullable=True
    )

    # =====================================================
    # Security
    # =====================================================

    failed_login_attempts = db.Column(
        db.Integer,
        nullable=False,
        default=0
    )

    locked_until = db.Column(
        db.DateTime,
        nullable=True
    )

    force_password_change = db.Column(
        db.Boolean,
        nullable=False,
        default=True
    )

    # =====================================================
    # Account Status
    # =====================================================

    account_status = db.Column(
        db.Enum(
            "Pending",
            "Active",
            "Suspended",
            "Locked",
            "Archived",
            name="user_account_status_enum"
        ),
        nullable=False,
        default="Pending",
        index=True
    )

    email_verified = db.Column(
        db.Boolean,
        nullable=False,
        default=False
    )

    phone_verified = db.Column(
        db.Boolean,
        nullable=False,
        default=False
    )

    two_factor_enabled = db.Column(
        db.Boolean,
        nullable=False,
        default=False
    )

    # =====================================================
    # Preferences
    # =====================================================

    preferred_language = db.Column(
        db.String(20),
        nullable=False,
        default="English"
    )

    # =====================================================
    # Internal Notes
    # =====================================================

    notes = db.Column(
        db.Text,
        nullable=True
    )

    # =====================================================
    # Relationships
    # =====================================================

    company = db.relationship(
        "Company",
        back_populates="users",
        lazy="joined"
    )

    role = db.relationship(
        "Role",
        back_populates="users",
        lazy="joined"
    )