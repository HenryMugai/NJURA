from database.db import db
from models.base import BaseModel


class Dashboard(BaseModel):
    """
    Stores dashboard preferences and configuration
    for individual users.

    Dashboard statistics are generated dynamically
    from operational data. This model stores only
    user preferences and layout settings.
    """

    __tablename__ = "dashboards"

    __table_args__ = (
        db.UniqueConstraint(
            "company_id",
            "user_id",
            name="uq_company_dashboard_user"
        ),
    )

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
    # Dashboard Information
    # =====================================================

    dashboard_name = db.Column(
        db.String(100),
        nullable=False,
        default="Default Dashboard"
    )

    dashboard_type = db.Column(
        db.Enum(
            "Super Admin",
            "Company Admin",
            "Distributor",
            "FSR",
            name="dashboard_type_enum"
        ),
        nullable=False,
        default="Company Admin"
    )

    # =====================================================
    # Layout Configuration
    # =====================================================

    layout = db.Column(
        db.JSON,
        nullable=True
    )

    widgets = db.Column(
        db.JSON,
        nullable=True
    )

    filters = db.Column(
        db.JSON,
        nullable=True
    )

    # =====================================================
    # Preferences
    # =====================================================

    default_dashboard = db.Column(
        db.Boolean,
        nullable=False,
        default=True
    )

    auto_refresh = db.Column(
        db.Boolean,
        nullable=False,
        default=True
    )

    refresh_interval = db.Column(
        db.Integer,
        nullable=False,
        default=300
    )

    # =====================================================
    # Status
    # =====================================================

    dashboard_status = db.Column(
        db.Enum(
            "Active",
            "Inactive",
            name="dashboard_status_enum"
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

    company = db.relationship(
        "Company",
        back_populates="dashboards",
        lazy="joined"
    )

    user = db.relationship(
        "User",
        back_populates="dashboards",
        lazy="joined"
    )

    # =====================================================
    # Object Representation
    # =====================================================

    def __repr__(self):
        return (
            f"<Dashboard("
            f"id={self.id}, "
            f"user_id={self.user_id}, "
            f"name='{self.dashboard_name}')>"
        )