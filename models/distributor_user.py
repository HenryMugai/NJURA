from datetime import date

from database.db import db
from models.base import BaseModel


class DistributorUser(BaseModel):
    """
    Associates a system user with a distributor.

    This allows a distributor to have one or more
    users accessing the platform while maintaining
    centralized authentication through the User model.
    """

    __tablename__ = "distributor_users"

    __table_args__ = (
        db.UniqueConstraint(
            "distributor_id",
            "user_id",
            name="uq_distributor_user"
        ),
    )

    # =====================================================
    # Foreign Keys
    # =====================================================

    distributor_id = db.Column(
        db.Integer,
        db.ForeignKey("distributors.id"),
        nullable=False,
        index=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False,
        index=True
    )

    # =====================================================
    # Assignment Information
    # =====================================================

    job_title = db.Column(
        db.String(100),
        nullable=True
    )

    is_primary_contact = db.Column(
        db.Boolean,
        nullable=False,
        default=False
    )

    assigned_date = db.Column(
        db.Date,
        nullable=False,
        default=date.today
    )

    # =====================================================
    # Status
    # =====================================================

    assignment_status = db.Column(
        db.Enum(
            "Active",
            "Inactive",
            name="distributor_user_status_enum"
        ),
        nullable=False,
        default="Active",
        index=True
    )

    # =====================================================
    # Notes
    # =====================================================

    notes = db.Column(
        db.Text,
        nullable=True
    )

    # =====================================================
    # Relationships
    # =====================================================

    distributor = db.relationship(
        "Distributor",
        back_populates="distributor_users",
        lazy="joined"
    )

    user = db.relationship(
        "User",
        back_populates="distributor_users",
        lazy="joined"
    )

    # =====================================================
    # Object Representation
    # =====================================================

    def __repr__(self):
        return (
            f"<DistributorUser("
            f"id={self.id}, "
            f"distributor_id={self.distributor_id}, "
            f"user_id={self.user_id})>"
        )