from database.db import db
from models.base import BaseModel


class Route(BaseModel):
    """
    Represents a sales route within a territory.

    A route belongs to a company and territory, and
    can later be assigned to an FSR and a distributor.
    """

    __tablename__ = "routes"

    __table_args__ = (
        db.UniqueConstraint(
            "company_id",
            "route_code",
            name="uq_company_route_code"
        ),
        db.UniqueConstraint(
            "company_id",
            "name",
            name="uq_company_route_name"
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

    route_code = db.Column(
        db.String(30),
        nullable=False
    )

    description = db.Column(
        db.Text,
        nullable=True
    )

    # =====================================================
    # Scheduling
    # =====================================================

    visit_frequency = db.Column(
        db.Enum(
            "Daily",
            "Weekly",
            "Bi-Weekly",
            "Monthly",
            name="route_visit_frequency_enum"
        ),
        nullable=False,
        default="Weekly"
    )

    visit_day = db.Column(
        db.Enum(
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
            name="route_visit_day_enum"
        ),
        nullable=True
    )

    # =====================================================
    # Route Information
    # =====================================================

    estimated_outlets = db.Column(
        db.Integer,
        nullable=False,
        default=0
    )

    estimated_visit_time = db.Column(
        db.Integer,
        nullable=True
    )

    # =====================================================
    # Status
    # =====================================================

    route_status = db.Column(
        db.Enum(
            "Active",
            "Inactive",
            name="route_status_enum"
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
        back_populates="routes",
        lazy="joined"
    )

    territory = db.relationship(
        "Territory",
        back_populates="routes",
        lazy="joined"
    )

    fsrs = db.relationship(
        "FSR",
        back_populates="route",
        lazy=True
    )

    outlets = db.relationship(
        "Outlet",
        back_populates="route",
        lazy=True
    )

    visits = db.relationship(
        "Visit",
        back_populates="route",
        lazy=True
    )

    orders = db.relationship(
        "Order",
        back_populates="route",
        lazy=True
    )

    # =====================================================
    # Object Representation
    # =====================================================

    def __repr__(self):
        return (
            f"<Route(id={self.id}, "
            f"name='{self.name}', "
            f"code='{self.route_code}')>"
        )