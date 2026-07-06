from database.db import db
from models.base import BaseModel


class AuditLog(BaseModel):
    """
    Records system activities performed by users.

    Audit logs provide a complete history of actions
    performed across the platform for accountability,
    troubleshooting and compliance.
    """

    __tablename__ = "audit_logs"

    # =====================================================
    # Foreign Keys
    # =====================================================

    company_id = db.Column(
        db.Integer,
        db.ForeignKey("companies.id"),
        nullable=True,
        index=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=True,
        index=True
    )

    # =====================================================
    # Activity Information
    # =====================================================

    module = db.Column(
        db.String(100),
        nullable=False,
        index=True
    )

    action = db.Column(
        db.String(100),
        nullable=False,
        index=True
    )

    description = db.Column(
        db.Text,
        nullable=False
    )

    # =====================================================
    # Affected Record
    # =====================================================

    entity_type = db.Column(
        db.String(100),
        nullable=True,
        index=True
    )

    entity_id = db.Column(
        db.Integer,
        nullable=True,
        index=True
    )

    # =====================================================
    # Change Tracking
    # =====================================================

    old_values = db.Column(
        db.JSON,
        nullable=True
    )

    new_values = db.Column(
        db.JSON,
        nullable=True
    )

    # =====================================================
    # Request Information
    # =====================================================

    ip_address = db.Column(
        db.String(45),
        nullable=True
    )

    user_agent = db.Column(
        db.Text,
        nullable=True
    )

    request_method = db.Column(
        db.String(10),
        nullable=True
    )

    request_url = db.Column(
        db.String(255),
        nullable=True
    )

    # =====================================================
    # Result
    # =====================================================

    status = db.Column(
        db.Enum(
            "Success",
            "Failed",
            "Warning",
            name="audit_log_status_enum"
        ),
        nullable=False,
        default="Success",
        index=True
    )

    # =====================================================
    # Additional Information
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
        back_populates="audit_logs",
        lazy="joined"
    )

    user = db.relationship(
        "User",
        back_populates="audit_logs",
        lazy="joined"
    )

    # =====================================================
    # Object Representation
    # =====================================================

    def __repr__(self):
        return (
            f"<AuditLog("
            f"id={self.id}, "
            f"module='{self.module}', "
            f"action='{self.action}')>"
        )