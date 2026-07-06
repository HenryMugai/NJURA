from database.db import db
from models.base import BaseModel


class Permission(BaseModel):
    """
    Defines a system permission.

    Permissions represent individual actions that can be
    performed within the platform. They are assigned to
    roles through the RolePermission model.
    """

    __tablename__ = "permissions"

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
    # Module
    # =====================================================

    module = db.Column(
        db.String(100),
        nullable=False,
        index=True
    )

    # =====================================================
    # System Configuration
    # =====================================================

    is_system_permission = db.Column(
        db.Boolean,
        nullable=False,
        default=True
    )

    # =====================================================
    # Status
    # =====================================================

    permission_status = db.Column(
        db.Enum(
            "Active",
            "Inactive",
            name="permission_status_enum"
        ),
        nullable=False,
        default="Active",
        index=True
    )

    # =====================================================
    # Relationships
    # =====================================================

    role_permissions = db.relationship(
        "RolePermission",
        back_populates="permission",
        lazy=True,
        cascade="all, delete-orphan"
    )

    # =====================================================
    # Object Representation
    # =====================================================

    def __repr__(self):
        return (
            f"<Permission(id={self.id}, "
            f"name='{self.name}')>"
        )