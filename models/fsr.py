from database.db import db
from models.base import BaseModel


class FSR(BaseModel):
    """
    Represents a Field Sales Representative (FSR).

    FSRs are responsible for:
        - Mapping outlets
        - Visiting outlets
        - Creating customer orders
        - Collecting market feedback
        - Executing assigned route plans
    """

    __tablename__ = "fsrs"

    __table_args__ = (
        db.UniqueConstraint(
            "company_id",
            "employee_number",
            name="uq_company_employee_number"
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
        unique=True,
        index=True
    )

    distributor_id = db.Column(
        db.Integer,
        db.ForeignKey("distributors.id"),
        nullable=False,
        index=True
    )

    territory_id = db.Column(
        db.Integer,
        db.ForeignKey("territories.id"),
        nullable=False,
        index=True
    )

    route_id = db.Column(
        db.Integer,
        db.ForeignKey("routes.id"),
        nullable=False,
        index=True
    )

    # =====================================================
    # Employment Information
    # =====================================================

    employee_number = db.Column(
        db.String(30),
        nullable=False
    )

    job_title = db.Column(
        db.String(100),
        nullable=True
    )

    date_employed = db.Column(
        db.Date,
        nullable=True
    )

    employment_type = db.Column(
        db.Enum(
            "Permanent",
            "Contract",
            "Temporary",
            "Intern",
            name="employment_type_enum"
        ),
        nullable=False,
        default="Permanent"
    )

    # =====================================================
    # Work Assignment
    # =====================================================

    supervisor = db.Column(
        db.String(150),
        nullable=True
    )

    device_id = db.Column(
        db.String(150),
        nullable=True
    )

    # =====================================================
    # Performance Targets
    # =====================================================

    daily_visit_target = db.Column(
        db.Integer,
        nullable=False,
        default=20
    )

    daily_order_target = db.Column(
        db.Integer,
        nullable=False,
        default=10
    )

    monthly_sales_target = db.Column(
        db.Numeric(12, 2),
        nullable=True
    )

    # =====================================================
    # GPS Settings
    # =====================================================

    gps_tracking_enabled = db.Column(
        db.Boolean,
        nullable=False,
        default=True
    )

    # =====================================================
    # Status
    # =====================================================

    fsr_status = db.Column(
        db.Enum(
            "Active",
            "Inactive",
            "Suspended",
            "On Leave",
            name="fsr_status_enum"
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
        back_populates="fsrs",
        lazy="joined"
    )

    user = db.relationship(
        "User",
        back_populates="fsr",
        lazy="joined"
    )

    distributor = db.relationship(
        "Distributor",
        back_populates="fsrs",
        lazy="joined"
    )

    territory = db.relationship(
        "Territory",
        back_populates="fsrs",
        lazy="joined"
    )

    route = db.relationship(
        "Route",
        back_populates="fsrs",
        lazy="joined"
    )

    outlets = db.relationship(
        "Outlet",
        back_populates="fsr",
        lazy=True
    )

    visits = db.relationship(
        "Visit",
        back_populates="fsr",
        lazy=True
    )

    visit_notes = db.relationship(
        "VisitNote",
        back_populates="fsr",
        lazy=True
    )

    orders = db.relationship(
        "Order",
        back_populates="fsr",
        lazy=True
    )

    deliveries = db.relationship(
        "Delivery",
        back_populates="fsr",
        lazy=True
    )

    # =====================================================
    # Object Representation
    # =====================================================

    def __repr__(self):
        return (
            f"<FSR("
            f"id={self.id}, "
            f"employee_number='{self.employee_number}', "
            f"user_id={self.user_id})>"
        )