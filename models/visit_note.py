from database.db import db
from models.base import BaseModel


class VisitNote(BaseModel):
    """
    Represents an observation or note recorded during
    a Field Sales Representative (FSR) visit.

    A single visit can have multiple notes.
    """

    __tablename__ = "visit_notes"

    # =====================================================
    # Foreign Keys
    # =====================================================

    company_id = db.Column(
        db.Integer,
        db.ForeignKey("companies.id"),
        nullable=False,
        index=True
    )

    visit_id = db.Column(
        db.Integer,
        db.ForeignKey("visits.id"),
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
    # Note Information
    # =====================================================

    title = db.Column(
        db.String(150),
        nullable=True
    )

    note = db.Column(
        db.Text,
        nullable=False
    )

    # =====================================================
    # Note Type
    # =====================================================

    note_type = db.Column(
        db.Enum(
            "General",
            "Customer Feedback",
            "Competitor Activity",
            "Product Display",
            "Promotion",
            "Stock Observation",
            "Follow Up",
            "Complaint",
            "Other",
            name="visit_note_type_enum"
        ),
        nullable=False,
        default="General",
        index=True
    )

    # =====================================================
    # Follow Up
    # =====================================================

    requires_follow_up = db.Column(
        db.Boolean,
        nullable=False,
        default=False
    )

    follow_up_date = db.Column(
        db.Date,
        nullable=True
    )

    # =====================================================
    # Status
    # =====================================================

    note_status = db.Column(
        db.Enum(
            "Open",
            "Closed",
            name="visit_note_status_enum"
        ),
        nullable=False,
        default="Open",
        index=True
    )

    # =====================================================
    # Relationships
    # =====================================================

    company = db.relationship(
        "Company",
        back_populates="visit_notes",
        lazy="joined"
    )

    visit = db.relationship(
        "Visit",
        back_populates="visit_notes",
        lazy="joined"
    )

    fsr = db.relationship(
        "FSR",
        back_populates="visit_notes",
        lazy="joined"
    )

    # =====================================================
    # Object Representation
    # =====================================================

    def __repr__(self):
        return (
            f"<VisitNote("
            f"id={self.id}, "
            f"visit_id={self.visit_id})>"
        )