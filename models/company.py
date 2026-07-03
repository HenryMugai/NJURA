from database.db import db
from models.base import BaseModel


class Company(BaseModel):
    """
    Represents a tenant (client company) within the
    N.J.U.R.A SaaS platform.

    Every business entity belongs to a company.
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

    business_type = db.Column(
        db.Enum(
            "Manufacturer",
            "Distributor",
            "Wholesaler",
            "Retailer",
            "Other",
            name="business_type_enum"
        ),
        nullable=False,
        default="Manufacturer"
    )

    industry = db.Column(
        db.String(100),
        nullable=False
    )

    # =====================================================
    # Contact Information
    # =====================================================

    email = db.Column(
        db.String(120),
        nullable=False,
        unique=True
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

    logo = db.Column(
        db.String(255),
        nullable=True
    )

    primary_color = db.Column(
        db.String(20),
        nullable=True
    )

    secondary_color = db.Column(
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

    is_verified = db.Column(
        db.Boolean,
        nullable=False,
        default=False
    )

    last_login_at = db.Column(
        db.DateTime,
        nullable=True
    )

    # =====================================================
    # Relationships
    # =====================================================

    # Relationships will be added after all
    # models have been completed.

    # =====================================================
    # Object Representation
    # =====================================================

    def __repr__(self):
        return (
            f"<Company(id={self.id}, "
            f"name='{self.name}', "
            f"code='{self.company_code}')>"
        )