from database.db import db
from models.base import BaseModel


class Product(BaseModel):
    """
    Represents a product sold by a company.

    Products belong to a category and can later
    have multiple prices, promotions and inventory
    records.
    """

    __tablename__ = "products"

    __table_args__ = (
        db.UniqueConstraint(
            "company_id",
            "product_code",
            name="uq_company_product_code"
        ),
        db.UniqueConstraint(
            "company_id",
            "sku",
            name="uq_company_product_sku"
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

    product_category_id = db.Column(
        db.Integer,
        db.ForeignKey("product_categories.id"),
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

    product_code = db.Column(
        db.String(30),
        nullable=False
    )

    sku = db.Column(
        db.String(100),
        nullable=False
    )

    barcode = db.Column(
        db.String(100),
        nullable=True
    )

    description = db.Column(
        db.Text,
        nullable=True
    )

    # =====================================================
    # Product Information
    # =====================================================

    brand = db.Column(
        db.String(100),
        nullable=True
    )

    unit_of_measure = db.Column(
        db.String(50),
        nullable=False,
        default="Piece"
    )

    pack_size = db.Column(
        db.String(100),
        nullable=True
    )

    weight = db.Column(
        db.Numeric(10, 2),
        nullable=True
    )

    # =====================================================
    # Product Image
    # =====================================================

    image_url = db.Column(
        db.String(255),
        nullable=True
    )

    # =====================================================
    # Business Rules
    # =====================================================

    minimum_order_quantity = db.Column(
        db.Integer,
        nullable=False,
        default=1
    )

    reorder_level = db.Column(
        db.Integer,
        nullable=True
    )

    tax_percentage = db.Column(
        db.Numeric(5, 2),
        nullable=False,
        default=16.00
    )

    # =====================================================
    # Status
    # =====================================================

    product_status = db.Column(
        db.Enum(
            "Active",
            "Inactive",
            "Discontinued",
            name="product_status_enum"
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
        back_populates="products",
        lazy="joined"
    )

    product_category = db.relationship(
        "ProductCategory",
        back_populates="products",
        lazy="joined"
    )

    product_prices = db.relationship(
        "ProductPrice",
        back_populates="product",
        lazy=True,
        cascade="all, delete-orphan"
    )

    order_items = db.relationship(
        "OrderItem",
        back_populates="product",
        lazy=True
    )

    # =====================================================
    # Object Representation
    # =====================================================

    def __repr__(self):
        return (
            f"<Product(id={self.id}, "
            f"name='{self.name}', "
            f"sku='{self.sku}')>"
        )