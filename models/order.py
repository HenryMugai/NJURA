from database.db import db
from models.base import BaseModel


class Order(BaseModel):
    """
    Represents a customer sales order.

    Orders are created by Field Sales Representatives
    during outlet visits and are fulfilled by distributors.
    """

    __tablename__ = "orders"

    __table_args__ = (
        db.UniqueConstraint(
            "company_id",
            "order_number",
            name="uq_company_order_number"
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

    outlet_id = db.Column(
        db.Integer,
        db.ForeignKey("outlets.id"),
        nullable=False,
        index=True
    )

    visit_id = db.Column(
        db.Integer,
        db.ForeignKey("visits.id"),
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

    route_id = db.Column(
        db.Integer,
        db.ForeignKey("routes.id"),
        nullable=False,
        index=True
    )

    # =====================================================
    # Order Information
    # =====================================================

    order_number = db.Column(
        db.String(50),
        nullable=False
    )

    order_date = db.Column(
        db.DateTime,
        nullable=False
    )

    requested_delivery_date = db.Column(
        db.Date,
        nullable=True
    )

    # =====================================================
    # Order Type
    # =====================================================

    order_type = db.Column(
        db.Enum(
            "Sale",
            "Replacement",
            "Return",
            "Sample",
            name="order_type_enum"
        ),
        nullable=False,
        default="Sale"
    )

    order_source = db.Column(
        db.Enum(
            "Mobile",
            "Web",
            "API",
            name="order_source_enum"
        ),
        nullable=False,
        default="Mobile"
    )

    # =====================================================
    # Financial Summary
    # =====================================================

    subtotal = db.Column(
        db.Numeric(12, 2),
        nullable=False,
        default=0.00
    )

    discount_amount = db.Column(
        db.Numeric(12, 2),
        nullable=False,
        default=0.00
    )

    tax_amount = db.Column(
        db.Numeric(12, 2),
        nullable=False,
        default=0.00
    )

    total_amount = db.Column(
        db.Numeric(12, 2),
        nullable=False,
        default=0.00
    )

    # =====================================================
    # Payment
    # =====================================================

    payment_status = db.Column(
        db.Enum(
            "Pending",
            "Partially Paid",
            "Paid",
            name="payment_status_enum"
        ),
        nullable=False,
        default="Pending",
        index=True
    )

    # =====================================================
    # Approval
    # =====================================================

    approval_status = db.Column(
        db.Enum(
            "Pending",
            "Approved",
            "Rejected",
            name="approval_status_enum"
        ),
        nullable=False,
        default="Pending",
        index=True
    )

    # =====================================================
    # Order Status
    # =====================================================

    order_status = db.Column(
        db.Enum(
            "Draft",
            "Submitted",
            "Processing",
            "Ready for Dispatch",
            "Dispatched",
            "Delivered",
            "Cancelled",
            name="order_status_enum"
        ),
        nullable=False,
        default="Submitted",
        index=True
    )

    # =====================================================
    # Remarks
    # =====================================================

    remarks = db.Column(
        db.Text,
        nullable=True
    )

    # =====================================================
    # Relationships
    # =====================================================

    company = db.relationship(
        "Company",
        back_populates="orders",
        lazy="joined"
    )

    outlet = db.relationship(
        "Outlet",
        back_populates="orders",
        lazy="joined"
    )

    visit = db.relationship(
        "Visit",
        back_populates="orders",
        lazy="joined"
    )

    distributor = db.relationship(
        "Distributor",
        back_populates="orders",
        lazy="joined"
    )

    fsr = db.relationship(
        "FSR",
        back_populates="orders",
        lazy="joined"
    )

    route = db.relationship(
        "Route",
        back_populates="orders",
        lazy="joined"
    )

    order_items = db.relationship(
        "OrderItem",
        back_populates="order",
        lazy=True,
        cascade="all, delete-orphan"
    )

    delivery = db.relationship(
        "Delivery",
        back_populates="order",
        uselist=False,
        lazy=True
    )

    # =====================================================
    # Object Representation
    # =====================================================

    def __repr__(self):
        return (
            f"<Order("
            f"id={self.id}, "
            f"number='{self.order_number}')>"
        )