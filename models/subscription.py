from datetime import datetime, timedelta

from database.db import db
from models.base import BaseModel


class Subscription(BaseModel):
    """
    Stores subscription information for each company.

    One company can only have one active subscription at a time,
    but historical subscriptions are retained for auditing
    and reporting purposes.
    """

    __tablename__ = "subscriptions"

    # ==========================================
    # Company
    # ==========================================

    company_id = db.Column(
        db.Integer,
        db.ForeignKey("companies.id"),
        nullable=False,
        index=True
    )

    # ==========================================
    # Subscription Details
    # ==========================================

    plan_name = db.Column(
        db.String(50),
        nullable=False
    )

    billing_cycle = db.Column(
        db.Enum(
            "Monthly",
            "Quarterly",
            "Bi-Annual",
            "Annual",
            name="subscription_billing_cycle"
        ),
        nullable=False,
        default="Monthly"
    )

    # ==========================================
    # Status
    # ==========================================

    status = db.Column(
        db.Enum(
            "Trial",
            "Active",
            "Expired",
            "Grace Period",
            "Suspended",
            "Cancelled",
            name="subscription_status"
        ),
        nullable=False,
        default="Trial",
        index=True
    )

    # ==========================================
    # Dates
    # ==========================================

    start_date = db.Column(
        db.Date,
        nullable=False,
        default=datetime.utcnow
    )

    end_date = db.Column(
        db.Date,
        nullable=False,
        default=lambda: (
            datetime.utcnow() + timedelta(days=30)
        ).date()
    )

    trial_end_date = db.Column(
        db.Date,
        nullable=True
    )

    grace_period_end = db.Column(
        db.Date,
        nullable=True
    )

    cancelled_at = db.Column(
        db.DateTime,
        nullable=True
    )

    # ==========================================
    # Financial
    # ==========================================

    amount = db.Column(
        db.Numeric(12, 2),
        nullable=False,
        default=0.00
    )

    currency = db.Column(
        db.String(10),
        nullable=False,
        default="KES"
    )

    # ==========================================
    # Payment Information
    # ==========================================

    last_payment_date = db.Column(
        db.DateTime,
        nullable=True
    )

    next_billing_date = db.Column(
        db.Date,
        nullable=True
    )

    payment_reference = db.Column(
        db.String(150),
        nullable=True
    )

    payment_method = db.Column(
        db.String(50),
        nullable=True
    )

    # ==========================================
    # Subscription Limits
    # ==========================================

    max_users = db.Column(
        db.Integer,
        nullable=False,
        default=20
    )

    max_fsrs = db.Column(
        db.Integer,
        nullable=False,
        default=10
    )

    max_products = db.Column(
        db.Integer,
        nullable=False,
        default=500
    )

    max_outlets = db.Column(
        db.Integer,
        nullable=False,
        default=1000
    )

    max_distributors = db.Column(
        db.Integer,
        nullable=False,
        default=20
    )

    # ==========================================
    # Features
    # ==========================================

    gps_tracking = db.Column(
        db.Boolean,
        default=True,
        nullable=False
    )

    analytics_enabled = db.Column(
        db.Boolean,
        default=True,
        nullable=False
    )

    api_access = db.Column(
        db.Boolean,
        default=False,
        nullable=False
    )

    offline_mode = db.Column(
        db.Boolean,
        default=False,
        nullable=False
    )

    # ==========================================
    # Internal Notes
    # ==========================================

    notes = db.Column(
        db.Text,
        nullable=True
    )

    # ==========================================
    # Relationships
    # ==========================================

    # Added after all models have been completed.

    def __repr__(self):
        return (
            f"<Subscription "
            f"{self.plan_name} "
            f"({self.status})>"
        )