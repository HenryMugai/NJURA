from database.db import db
from models.base import BaseModel


class Notification(BaseModel):
    """
    Represents a notification sent to a user.

    Notifications may be generated automatically
    by the system or manually by administrators.
    """

    __tablename__ = "notifications"

    # =====================================================
    # Foreign Keys
    # =====================================================

    company_id = db.Column(
        db.Integer,
        db.ForeignKey("companies.id"),
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
    # Notification Information
    # =====================================================

    title = db.Column(
        db.String(200),
        nullable=False
    )

    message = db.Column(
        db.Text,
        nullable=False
    )

    notification_type = db.Column(
        db.Enum(
            "System",
            "Order",
            "Delivery",
            "Visit",
            "Product",
            "Reminder",
            "Announcement",
            "Warning",
            "Success",
            name="notification_type_enum"
        ),
        nullable=False,
        default="System",
        index=True
    )

    # =====================================================
    # Delivery Channel
    # =====================================================

    delivery_channel = db.Column(
        db.Enum(
            "In-App",
            "Email",
            "SMS",
            "Push",
            name="notification_channel_enum"
        ),
        nullable=False,
        default="In-App"
    )

    # =====================================================
    # Notification Status
    # =====================================================

    notification_status = db.Column(
        db.Enum(
            "Pending",
            "Sent",
            "Delivered",
            "Read",
            "Failed",
            name="notification_status_enum"
        ),
        nullable=False,
        default="Pending",
        index=True
    )

    is_read = db.Column(
        db.Boolean,
        nullable=False,
        default=False
    )

    read_at = db.Column(
        db.DateTime,
        nullable=True
    )

    # =====================================================
    # Navigation
    # =====================================================

    action_url = db.Column(
        db.String(255),
        nullable=True
    )

    reference_type = db.Column(
        db.String(100),
        nullable=True
    )

    reference_id = db.Column(
        db.Integer,
        nullable=True
    )

    # =====================================================
    # Scheduling
    # =====================================================

    scheduled_at = db.Column(
        db.DateTime,
        nullable=True
    )

    sent_at = db.Column(
        db.DateTime,
        nullable=True
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

    company = db.relationship(
        "Company",
        back_populates="notifications",
        lazy="joined"
    )

    user = db.relationship(
        "User",
        back_populates="notifications",
        lazy="joined"
    )

    # =====================================================
    # Object Representation
    # =====================================================

    def __repr__(self):
        return (
            f"<Notification("
            f"id={self.id}, "
            f"user_id={self.user_id}, "
            f"title='{self.title}')>"
        )