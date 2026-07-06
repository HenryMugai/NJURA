from database.db import db
from models.base import BaseModel


class OrderItem(BaseModel):
    """
    Represents an individual product line within
    a customer order.

    Product details and pricing are stored as a
    snapshot to preserve historical accuracy.
    """

    __tablename__ = "order_items"

    # =====================================================
    # Foreign Keys
    # =====================================================

    company_id = db.Column(
        db.Integer,
        db.ForeignKey("companies.id"),
        nullable=False,
        index=True
    )

    order_id = db.Column(
        db.Integer,
        db.ForeignKey("orders.id"),
        nullable=False,
        index=True
    )

    product_id = db.Column(
        db.Integer,
        db.ForeignKey("products.id"),
        nullable=False,
        index=True
    )

    product_price_id = db.Column(
        db.Integer,
        db.ForeignKey("product_prices.id"),
        nullable=True,
        index=True
    )

    # =====================================================
    # Product Snapshot
    # =====================================================

    product_name = db.Column(
        db.String(150),
        nullable=False
    )

    sku = db.Column(
        db.String(100),
        nullable=True
    )

    unit_of_measure = db.Column(
        db.String(50),
        nullable=True
    )

    # =====================================================
    # Quantities
    # =====================================================

    quantity = db.Column(
        db.Integer,
        nullable=False,
        default=1
    )

    free_quantity = db.Column(
        db.Integer,
        nullable=False,
        default=0
    )

    # =====================================================
    # Pricing
    # =====================================================

    unit_price = db.Column(
        db.Numeric(12, 2),
        nullable=False
    )

    discount_percentage = db.Column(
        db.Numeric(5, 2),
        nullable=False,
        default=0.00
    )

    discount_amount = db.Column(
        db.Numeric(12, 2),
        nullable=False,
        default=0.00
    )

    tax_percentage = db.Column(
        db.Numeric(5, 2),
        nullable=False,
        default=0.00
    )

    tax_amount = db.Column(
        db.Numeric(12, 2),
        nullable=False,
        default=0.00
    )

    line_total = db.Column(
        db.Numeric(12, 2),
        nullable=False,
        default=0.00
    )

    # =====================================================
    # Status
    # =====================================================

    item_status = db.Column(
        db.Enum(
            "Pending",
            "Approved",
            "Rejected",
            "Cancelled",
            name="order_item_status_enum"
        ),
        nullable=False,
        default="Pending",
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
        back_populates="order_items",
        lazy="joined"
    )

    order = db.relationship(
        "Order",
        back_populates="order_items",
        lazy="joined"
    )

    product = db.relationship(
        "Product",
        back_populates="order_items",
        lazy="joined"
    )

    product_price = db.relationship(
        "ProductPrice",
        back_populates="order_items",
        lazy="joined"
    )

    # =====================================================
    # Object Representation
    # =====================================================

    def __repr__(self):
        return (
            f"<OrderItem("
            f"id={self.id}, "
            f"order_id={self.order_id}, "
            f"product='{self.product_name}')>"
        )