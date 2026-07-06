from database.db import db
from models.base import BaseModel


class Territory(BaseModel):
    """
    Represents a sales territory within a company.

    Territories help organize distributors,
    routes, FSRs and retail outlets.
    """

    __tablename__ = "territories"

    __table_args__ = (
        db.UniqueConstraint(
            "company_id",
            "code",
            name="uq_company_territory_code"
        ),
        db.UniqueConstraint(
            "company_id",
            "name",
            name="uq_company_territory_name"
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

    # =====================================================
    # Basic Information
    # =====================================================

    name = db.Column(
        db.String(150),
        nullable=False
    )

    code = db.Column(
        db.String(30),
        nullable=False
    )

    description = db.Column(
        db.Text,
        nullable=True
    )

    # =====================================================
    # Geographic Information
    # =====================================================

    county = db.Column(
        db.String(100),
        nullable=True
    )

    sub_county = db.Column(
        db.String(100),
        nullable=True
    )

    ward = db.Column(
        db.String(100),
        nullable=True
    )

    town = db.Column(
        db.String(100),
        nullable=True
    )

    # =====================================================
    # Status
    # =====================================================

    territory_status = db.Column(
        db.Enum(
            "Active",
            "Inactive",
            name="territory_status_enum"
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
        back_populates="territories",
        lazy="joined"
    )

    routes = db.relationship(
        "Route",
        back_populates="territory",
        lazy=True
    )

    distributors = db.relationship(
        "Distributor",
        back_populates="territory",
        lazy=True
    )

    fsrs = db.relationship(
        "FSR",
        back_populates="territory",
        lazy=True
    )

    outlets = db.relationship(
        "Outlet",
        back_populates="territory",
        lazy=True
    )

    # =====================================================
    # Object Representation
    # =====================================================

    def __repr__(self):
        return (
            f"<Territory(id={self.id}, "
            f"name='{self.name}', "
            f"code='{self.code}')>"
        )