from database.db import db
from models.base import BaseModel


class ProductPrice(BaseModel):
    """
    Represents the selling price of a product.

    Keeping prices in a separate table allows
    price history, future promotions and pricing
    revisions without modifying the Product table.
    """

    __tablename__ = "product_prices"

    # =====================================================
    # Foreign Keys
    # =====================================================

    company_id = db.Column(
        db.Integer,
        db.ForeignKey("companies.id"),
        nullable=False,
        index=True
    )

    product_id = db.Column(
        db.Integer,
        db.ForeignKey("products.id"),
        nullable=False,
        index=True
    )

    # =====================================================
    # Pricing Information
    # =====================================================

    selling_price = db.Column(
        db.Numeric(12, 2),
        nullable=False
    )

    minimum_selling_price = db.Column(
        db.Numeric(12, 2),
        nullable=True
    )

    maximum_selling_price = db.Column(
        db.Numeric(12, 2),
        nullable=True
    )

    currency = db.Column(
        db.String(10),
        nullable=False,
        default="KES"
    )

    # =====================================================
    # Effective Period
    # =====================================================

    effective_from = db.Column(
        db.Date,
        nullable=False
    )

    effective_to = db.Column(
        db.Date,
        nullable=True
    )

    # =====================================================
    # Status
    # =====================================================

    price_status = db.Column(
        db.Enum(
            "Active",
            "Expired",
            "Scheduled",
            name="product_price_status_enum"
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
        back_populates="product_prices",
        lazy="joined"
    )

    product = db.relationship(
        "Product",
        back_populates="product_prices",
        lazy="joined"
    )

    order_items = db.relationship(
        "OrderItem",
        back_populates="product_price",
        lazy=True
    )

    # =====================================================
    # Object Representation
    # =====================================================

    def __repr__(self):
        return (
            f"<ProductPrice("
            f"product_id={self.product_id}, "
            f"selling_price={self.selling_price})>"
        )