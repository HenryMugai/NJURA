from database.db import db
from models.base import BaseModel


class ProductCategory(BaseModel):
    """
    Represents a product category.

    Product categories help organize products for
    reporting, filtering and inventory management.
    """

    __tablename__ = "product_categories"

    __table_args__ = (
        db.UniqueConstraint(
            "company_id",
            "name",
            name="uq_company_product_category_name"
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

    category_code = db.Column(
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
            name="product_category_status_enum"
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
        back_populates="product_categories",
        lazy="joined"
    )

    products = db.relationship(
        "Product",
        back_populates="product_category",
        lazy=True
    )

    # =====================================================
    # Object Representation
    # =====================================================

    def __repr__(self):
        return (
            f"<ProductCategory(id={self.id}, "
            f"name='{self.name}')>"
        )