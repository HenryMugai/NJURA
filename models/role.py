from database.db import db
from models.base import BaseModel


class Role(BaseModel):
    """
    Defines system-wide user roles.

    Roles are global across the N.J.U.R.A platform and
    are linked to users through the User model and
    permissions through the RolePermission model.
    """

    __tablename__ = "roles"

    # =====================================================
    # Basic Information
    # =====================================================

    name = db.Column(
        db.String(100),
        nullable=False,
        unique=True,
        index=True
    )

    display_name = db.Column(
        db.String(150),
        nullable=False
    )

    description = db.Column(
        db.Text,
        nullable=True
    )

    # =====================================================
    # System Configuration
    # =====================================================

    is_system_role = db.Column(
        db.Boolean,
        nullable=False,
        default=True
    )

    priority = db.Column(
        db.Integer,
        nullable=False,
        default=100
    )

    # =====================================================
    # Status
    # =====================================================

    role_status = db.Column(
        db.Enum(
            "Active",
            "Inactive",
            name="role_status_enum"
        ),
        nullable=False,
        default="Active",
        index=True
    )

    # =====================================================
    # Relationships
    # =====================================================

    users = db.relationship(
        "User",
        back_populates="role",
        lazy=True
    )

    role_permissions = db.relationship(
        "RolePermission",
        back_populates="role",
        lazy=True,
        cascade="all, delete-orphan"
    )

    # =====================================================
    # Object Representation
    # =====================================================

    def __repr__(self):
        return (
            f"<Role(id={self.id}, "
            f"name='{self.name}')>"
        )