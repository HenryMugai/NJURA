from database.db import db
from models.base import BaseModel


class Outlet(BaseModel):
    """
    Represents a customer retail outlet.

    Outlets are registered by Field Sales Representatives
    and become the primary customers within the platform.
    """

    __tablename__ = "outlets"

    __table_args__ = (
        db.UniqueConstraint(
            "company_id",
            "outlet_code",
            name="uq_company_outlet_code"
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

    outlet_category_id = db.Column(
        db.Integer,
        db.ForeignKey("outlet_categories.id"),
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

    distributor_id = db.Column(
        db.Integer,
        db.ForeignKey("distributors.id"),
        nullable=False,
        index=True
    )

    fsr_id = db.Column(
        db.Integer,
        db.ForeignKey("fsrs.id"),
        nullable=False,
        index=True
    )

    # =====================================================
    # Basic Information
    # =====================================================

    name = db.Column(
        db.String(150),
        nullable=False,
        index=True
    )

    outlet_code = db.Column(
        db.String(30),
        nullable=False
    )

    description = db.Column(
        db.Text,
        nullable=True
    )

    # =====================================================
    # Owner Information
    # =====================================================

    owner_name = db.Column(
        db.String(150),
        nullable=True
    )

    owner_phone = db.Column(
        db.String(20),
        nullable=True
    )

    owner_email = db.Column(
        db.String(120),
        nullable=True
    )

    # =====================================================
    # Contact Information
    # =====================================================

    phone = db.Column(
        db.String(20),
        nullable=True
    )

    alternative_phone = db.Column(
        db.String(20),
        nullable=True
    )

    email = db.Column(
        db.String(120),
        nullable=True
    )

    # =====================================================
    # Physical Address
    # =====================================================

    address = db.Column(
        db.Text,
        nullable=True
    )

    town = db.Column(
        db.String(100),
        nullable=True
    )

    county = db.Column(
        db.String(100),
        nullable=True
    )

    landmark = db.Column(
        db.String(255),
        nullable=True
    )

    # =====================================================
    # GPS Coordinates
    # =====================================================

    latitude = db.Column(
        db.Numeric(10, 8),
        nullable=True
    )

    longitude = db.Column(
        db.Numeric(11, 8),
        nullable=True
    )

    # =====================================================
    # Business Information
    # =====================================================

    business_since = db.Column(
        db.Date,
        nullable=True
    )

    average_monthly_sales = db.Column(
        db.Numeric(12, 2),
        nullable=True
    )

    credit_limit = db.Column(
        db.Numeric(12, 2),
        nullable=True,
        default=0.00
    )

    opening_balance = db.Column(
        db.Numeric(12, 2),
        nullable=True,
        default=0.00
    )

    # =====================================================
    # Visit Information
    # =====================================================

    preferred_visit_day = db.Column(
        db.Enum(
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
            name="preferred_visit_day_enum"
        ),
        nullable=True
    )

    last_visit_date = db.Column(
        db.Date,
        nullable=True
    )

    last_order_date = db.Column(
        db.Date,
        nullable=True
    )

    # =====================================================
    # Status
    # =====================================================

    outlet_status = db.Column(
        db.Enum(
            "Active",
            "Inactive",
            "Closed",
            name="outlet_status_enum"
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
        back_populates="outlets",
        lazy="joined"
    )

    outlet_category = db.relationship(
        "OutletCategory",
        back_populates="outlets",
        lazy="joined"
    )

    territory = db.relationship(
        "Territory",
        back_populates="outlets",
        lazy="joined"
    )

    route = db.relationship(
        "Route",
        back_populates="outlets",
        lazy="joined"
    )

    distributor = db.relationship(
        "Distributor",
        back_populates="outlets",
        lazy="joined"
    )

    fsr = db.relationship(
        "FSR",
        back_populates="outlets",
        lazy="joined"
    )

    visits = db.relationship(
        "Visit",
        back_populates="outlet",
        lazy=True
    )

    orders = db.relationship(
        "Order",
        back_populates="outlet",
        lazy=True
    )

    deliveries = db.relationship(
        "Delivery",
        back_populates="outlet",
        lazy=True
    )

    # =====================================================
    # Object Representation
    # =====================================================

    def __repr__(self):
        return (
            f"<Outlet(id={self.id}, "
            f"name='{self.name}', "
            f"code='{self.outlet_code}')>"
        )