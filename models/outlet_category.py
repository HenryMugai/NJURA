from database.db import db
from models.base import BaseModel


class OutletCategory(BaseModel):
    """
    Represents a category of retail outlet.

    Outlet categories help classify customers for
    reporting, route planning and sales analysis.
    """

    __tablename__ = "outlet_categories"

    __table_args__ = (
        db.UniqueConstraint(
            "company_id",
            "name",
            name="uq_company_outlet_category_name"
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
        db.String(100),
        nullable=False
    )

    code = db.Column(
        db.String(30),
        nullable=True
    )

    description = db.Column(
        db.Text,
        nullable=True
    )

    # =====================================================
    # Status
    # =====================================================

    category_status = db.Column(
        db.Enum(
            "Active",
            "Inactive",
            name="outlet_category_status_enum"
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
        back_populates="outlet_categories",
        lazy="joined"
    )

    outlets = db.relationship(
        "Outlet",
        back_populates="outlet_category",
        lazy=True
    )

    # =====================================================
    # Object Representation
    # =====================================================

    def __repr__(self):
        return (
            f"<OutletCategory("
            f"id={self.id}, "
            f"name='{self.name}')>"
        )