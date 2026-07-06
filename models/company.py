from database.db import db
from models.base import BaseModel


class Company(BaseModel):
    """
    Represents a tenant (client company) within the
    N.J.U.R.A SaaS platform.

    Every operational record in the system belongs
    to a company.
    """

    __tablename__ = "companies"

    # =====================================================
    # Basic Information
    # =====================================================

    name = db.Column(
        db.String(150),
        nullable=False,
        unique=True,
        index=True
    )

    company_code = db.Column(
        db.String(20),
        nullable=False,
        unique=True,
        index=True
    )

    slug = db.Column(
        db.String(180),
        nullable=False,
        unique=True,
        index=True
    )

    description = db.Column(
        db.Text,
        nullable=True
    )

    industry = db.Column(
        db.String(100),
        nullable=True
    )

    initials = db.Column(
        db.String(10),
        nullable=True
    )

    # =====================================================
    # Contact Information
    # =====================================================

    email = db.Column(
        db.String(120),
        nullable=False,
        unique=True,
        index=True
    )

    phone = db.Column(
        db.String(20),
        nullable=False
    )

    alternative_phone = db.Column(
        db.String(20),
        nullable=True
    )

    website = db.Column(
        db.String(255),
        nullable=True
    )

    # =====================================================
    # Primary Contact Person
    # =====================================================

    contact_person = db.Column(
        db.String(150),
        nullable=True
    )

    contact_person_phone = db.Column(
        db.String(20),
        nullable=True
    )

    contact_person_email = db.Column(
        db.String(120),
        nullable=True
    )

    # =====================================================
    # Registration Information
    # =====================================================

    registration_number = db.Column(
        db.String(50),
        nullable=True,
        unique=True
    )

    kra_pin = db.Column(
        db.String(20),
        nullable=True,
        unique=True
    )

    # =====================================================
    # Branding
    # =====================================================

    logo_url = db.Column(
        db.String(255),
        nullable=True
    )

    brand_primary_color = db.Column(
        db.String(20),
        nullable=True
    )

    brand_secondary_color = db.Column(
        db.String(20),
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

    country = db.Column(
        db.String(100),
        nullable=False,
        default="Kenya"
    )

    postal_address = db.Column(
        db.String(100),
        nullable=True
    )

    postal_code = db.Column(
        db.String(20),
        nullable=True
    )

    # =====================================================
    # System Settings
    # =====================================================

    timezone = db.Column(
        db.String(100),
        nullable=False,
        default="Africa/Nairobi"
    )

    currency = db.Column(
        db.String(10),
        nullable=False,
        default="KES"
    )

    date_format = db.Column(
        db.String(20),
        nullable=False,
        default="DD/MM/YYYY"
    )

    # =====================================================
    # Company Preferences
    # =====================================================

    allow_outlet_creation = db.Column(
        db.Boolean,
        nullable=False,
        default=True
    )

    allow_order_editing = db.Column(
        db.Boolean,
        nullable=False,
        default=True
    )

    require_visit_before_order = db.Column(
        db.Boolean,
        nullable=False,
        default=True
    )

    # =====================================================
    # Account Status
    # =====================================================

    company_status = db.Column(
        db.Enum(
            "Pending",
            "Active",
            "Suspended",
            "Archived",
            name="company_status_enum"
        ),
        nullable=False,
        default="Pending",
        index=True
    )

    is_verified = db.Column(
        db.Boolean,
        nullable=False,
        default=False
    )

    onboarding_completed = db.Column(
        db.Boolean,
        nullable=False,
        default=False
    )

    # =====================================================
    # Internal Notes
    # =====================================================

    notes = db.Column(
        db.Text,
        nullable=True
    )

    # =====================================================
    # Relationships
    # =====================================================

    subscriptions = db.relationship(
        "Subscription",
        back_populates="company",
        lazy=True
    )

    users = db.relationship(
        "User",
        back_populates="company",
        lazy=True
    )

    territories = db.relationship(
        "Territory",
        back_populates="company",
        lazy=True
    )

    routes = db.relationship(
        "Route",
        back_populates="company",
        lazy=True
    )

    distributors = db.relationship(
        "Distributor",
        back_populates="company",
        lazy=True
    )

    outlet_categories = db.relationship(
        "OutletCategory",
        back_populates="company",
        lazy=True
    )

    outlets = db.relationship(
        "Outlet",
        back_populates="company",
        lazy=True
    )

    fsrs = db.relationship(
        "FSR",
        back_populates="company",
        lazy=True
    )

    product_categories = db.relationship(
        "ProductCategory",
        back_populates="company",
        lazy=True
    )

    products = db.relationship(
        "Product",
        back_populates="company",
        lazy=True
    )

    product_prices = db.relationship(
        "ProductPrice",
        back_populates="company",
        lazy=True
    )

    visits = db.relationship(
        "Visit",
        back_populates="company",
        lazy=True
    )

    visit_notes = db.relationship(
        "VisitNote",
        back_populates="company",
        lazy=True
    )

    orders = db.relationship(
        "Order",
        back_populates="company",
        lazy=True
    )

    order_items = db.relationship(
        "OrderItem",
        back_populates="company",
        lazy=True
    )

    deliveries = db.relationship(
        "Delivery",
        back_populates="company",
        lazy=True
    )

    dashboards = db.relationship(
        "Dashboard",
        back_populates="company",
        lazy=True
    )

    notifications = db.relationship(
        "Notification",
        back_populates="company",
        lazy=True
    )

    audit_logs = db.relationship(
        "AuditLog",
        back_populates="company",
        lazy=True
    )

    # =====================================================
    # Object Representation
    # =====================================================

    def __repr__(self):
        return (
            f"<Company(id={self.id}, "
            f"name='{self.name}', "
            f"code='{self.company_code}')>"
        )