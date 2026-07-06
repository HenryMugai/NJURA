from database.db import db
from models.base import BaseModel


class Visit(BaseModel):
    """
    Represents a Field Sales Representative (FSR)
    visit to an outlet.

    A visit may or may not result in an order.
    """

    __tablename__ = "visits"

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

    fsr_id = db.Column(
        db.Integer,
        db.ForeignKey("fsrs.id"),
        nullable=False,
        index=True
    )

    distributor_id = db.Column(
        db.Integer,
        db.ForeignKey("distributors.id"),
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
    # Visit Information
    # =====================================================

    visit_date = db.Column(
        db.Date,
        nullable=False,
        index=True
    )

    check_in_time = db.Column(
        db.DateTime,
        nullable=False
    )

    check_out_time = db.Column(
        db.DateTime,
        nullable=True
    )

    visit_duration = db.Column(
        db.Integer,
        nullable=True
    )

    # =====================================================
    # GPS Information
    # =====================================================

    check_in_latitude = db.Column(
        db.Numeric(10, 8),
        nullable=True
    )

    check_in_longitude = db.Column(
        db.Numeric(11, 8),
        nullable=True
    )

    check_out_latitude = db.Column(
        db.Numeric(10, 8),
        nullable=True
    )

    check_out_longitude = db.Column(
        db.Numeric(11, 8),
        nullable=True
    )

    # =====================================================
    # Visit Outcome
    # =====================================================

    visit_outcome = db.Column(
        db.Enum(
            "Successful",
            "Order Placed",
            "Outlet Closed",
            "Owner Absent",
            "No Stock Required",
            "Follow Up Required",
            "Survey",
            name="visit_outcome_enum"
        ),
        nullable=False,
        default="Successful",
        index=True
    )

    # =====================================================
    # Business Information
    # =====================================================

    customer_feedback = db.Column(
        db.Text,
        nullable=True
    )

    competitor_activity = db.Column(
        db.Text,
        nullable=True
    )

    stock_observation = db.Column(
        db.Text,
        nullable=True
    )

    # =====================================================
    # Status
    # =====================================================

    visit_status = db.Column(
        db.Enum(
            "Open",
            "Completed",
            "Cancelled",
            name="visit_status_enum"
        ),
        nullable=False,
        default="Open",
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
        back_populates="visits",
        lazy="joined"
    )

    outlet = db.relationship(
        "Outlet",
        back_populates="visits",
        lazy="joined"
    )

    fsr = db.relationship(
        "FSR",
        back_populates="visits",
        lazy="joined"
    )

    distributor = db.relationship(
        "Distributor",
        back_populates="visits",
        lazy="joined"
    )

    route = db.relationship(
        "Route",
        back_populates="visits",
        lazy="joined"
    )

    visit_notes = db.relationship(
        "VisitNote",
        back_populates="visit",
        lazy=True,
        cascade="all, delete-orphan"
    )

    orders = db.relationship(
        "Order",
        back_populates="visit",
        lazy=True
    )

    # =====================================================
    # Object Representation
    # =====================================================

    def __repr__(self):
        return (
            f"<Visit("
            f"id={self.id}, "
            f"outlet_id={self.outlet_id}, "
            f"fsr_id={self.fsr_id})>"
        )