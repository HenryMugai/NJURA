from database.db import db
from models.base import BaseModel


class Distributor(BaseModel):
    """
    Represents a distributor belonging to a company.

    Distributors receive and fulfill customer orders
    submitted by Field Sales Representatives (FSRs).
    """

    __tablename__ = "distributors"

    __table_args__ = (
        db.UniqueConstraint(
            "company_id",
            "distributor_code",
            name="uq_company_distributor_code"
        ),
        db.UniqueConstraint(
            "company_id",
            "name",
            name="uq_company_distributor_name"
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

    territory_id = db.Column(
        db.Integer,
        db.ForeignKey("territories.id"),
        nullable=True,
        index=True
    )

    # =====================================================
    # Basic Information
    # =====================================================

    name = db.Column(
        db.String(150),
        nullable=False
    )

    distributor_code = db.Column(
        db.String(30),
        nullable=False
    )

    description = db.Column(
        db.Text,
        nullable=True
    )

    # =====================================================
    # Business Information
    # =====================================================

    kra_pin = db.Column(
        db.String(20),
        nullable=True
    )

    registration_number = db.Column(
        db.String(50),
        nullable=True
    )

    # =====================================================
    # Contact Information
    # =====================================================

    email = db.Column(
        db.String(120),
        nullable=True
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
    # Contact Person
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

    postal_address = db.Column(
        db.String(100),
        nullable=True
    )

    postal_code = db.Column(
        db.String(20),
        nullable=True
    )

    # =====================================================
    # Status
    # =====================================================

    distributor_status = db.Column(
        db.Enum(
            "Active",
            "Inactive",
            "Suspended",
            name="distributor_status_enum"
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
        back_populates="distributors",
        lazy="joined"
    )

    territory = db.relationship(
        "Territory",
        back_populates="distributors",
        lazy="joined"
    )

    distributor_users = db.relationship(
        "DistributorUser",
        back_populates="distributor",
        lazy=True
    )

    fsrs = db.relationship(
        "FSR",
        back_populates="distributor",
        lazy=True
    )

    outlets = db.relationship(
        "Outlet",
        back_populates="distributor",
        lazy=True
    )

    orders = db.relationship(
        "Order",
        back_populates="distributor",
        lazy=True
    )

    deliveries = db.relationship(
        "Delivery",
        back_populates="distributor",
        lazy=True
    )

    # =====================================================
    # Object Representation
    # =====================================================

    def __repr__(self):
        return (
            f"<Distributor(id={self.id}, "
            f"name='{self.name}', "
            f"code='{self.distributor_code}')>"
        )