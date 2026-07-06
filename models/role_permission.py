from database.db import db
from models.base import BaseModel


class RolePermission(BaseModel):
    """
    Associates roles with permissions.

    Each record grants a specific permission
    to a specific role.
    """

    __tablename__ = "role_permissions"

    __table_args__ = (
        db.UniqueConstraint(
            "role_id",
            "permission_id",
            name="uq_role_permission"
        ),
    )

    # =====================================================
    # Foreign Keys
    # =====================================================

    role_id = db.Column(
        db.Integer,
        db.ForeignKey("roles.id"),
        nullable=False,
        index=True
    )

    permission_id = db.Column(
        db.Integer,
        db.ForeignKey("permissions.id"),
        nullable=False,
        index=True
    )

    # =====================================================
    # Status
    # =====================================================

    is_allowed = db.Column(
        db.Boolean,
        nullable=False,
        default=True
    )

    # =====================================================
    # Relationships
    # =====================================================

    role = db.relationship(
        "Role",
        back_populates="role_permissions",
        lazy="joined"
    )

    permission = db.relationship(
        "Permission",
        back_populates="role_permissions",
        lazy="joined"
    )

    # =====================================================
    # Object Representation
    # =====================================================

    def __repr__(self):
        return (
            f"<RolePermission("
            f"role_id={self.role_id}, "
            f"permission_id={self.permission_id})>"
        )