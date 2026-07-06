from database.db import db
from models.base import BaseModel


class Delivery(BaseModel):
    """
    Represents the delivery of a customer order.

    Deliveries are managed by distributors and
    track the lifecycle of an order from dispatch
    to successful delivery.
    """

    __tablename__ = "deliveries"

    __table_args__ = (
        db.UniqueConstraint(
            "company_id",
            "delivery_number",
            name="uq_company_delivery_number"
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

    order_id = db.Column(
        db.Integer,
        db.ForeignKey("orders.id"),
        nullable=False,
        unique=True,
        index=True
    )

    distributor_id = db.Column(
        db.Integer,
        db.ForeignKey("distributors.id"),
        nullable=False,
        index=True
    )

    outlet_id = db.Column(
        db.Integer,
        db.ForeignKey("outlets.id"),
        nullable=False,
        index=True
    )

    fsr_id = db.Column(
        db.Integer,
        db.ForeignKey("fsrs.id"),
        nullable=False,
        index=True
    )

    # =====================================================
    # Delivery Information
    # =====================================================

    delivery_number = db.Column(
        db.String(50),
        nullable=False
    )

    dispatch_date = db.Column(
        db.DateTime,
        nullable=True
    )

    expected_delivery_date = db.Column(
        db.Date,
        nullable=True
    )

    delivered_date = db.Column(
        db.DateTime,
        nullable=True
    )

    # =====================================================
    # Delivery Contact
    # =====================================================

    delivered_to = db.Column(
        db.String(150),
        nullable=True
    )

    recipient_phone = db.Column(
        db.String(20),
        nullable=True
    )

    # =====================================================
    # Delivery Status
    # =====================================================

    delivery_status = db.Column(
        db.Enum(
            "Pending",
            "Preparing",
            "Dispatched",
            "In Transit",
            "Delivered",
            "Partially Delivered",
            "Failed",
            "Returned",
            "Cancelled",
            name="delivery_status_enum"
        ),
        nullable=False,
        default="Pending",
        index=True
    )

    # =====================================================
    # Delivery Remarks
    # =====================================================

    failure_reason = db.Column(
        db.Text,
        nullable=True
    )

    customer_comments = db.Column(
        db.Text,
        nullable=True
    )

    internal_notes = db.Column(
        db.Text,
        nullable=True
    )

    # =====================================================
    # Proof of Delivery
    # =====================================================

    proof_of_delivery = db.Column(
        db.String(255),
        nullable=True
    )

    recipient_signature = db.Column(
        db.String(255),
        nullable=True
    )

    # =====================================================
    # Relationships
    # =====================================================

    company = db.relationship(
        "Company",
        back_populates="deliveries",
        lazy="joined"
    )

    order = db.relationship(
        "Order",
        back_populates="delivery",
        lazy="joined"
    )

    distributor = db.relationship(
        "Distributor",
        back_populates="deliveries",
        lazy="joined"
    )

    outlet = db.relationship(
        "Outlet",
        back_populates="deliveries",
        lazy="joined"
    )

    fsr = db.relationship(
        "FSR",
        back_populates="deliveries",
        lazy="joined"
    )

    # =====================================================
    # Object Representation
    # =====================================================

    def __repr__(self):
        return (
            f"<Delivery("
            f"id={self.id}, "
            f"delivery_number='{self.delivery_number}')>"
        )