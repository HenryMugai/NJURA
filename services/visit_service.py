"""
Visit Service

Handles business logic related to
Field Sales Representative (FSR) visits.
"""

from datetime import datetime

from database.db import db
from models import Visit, VisitNote, Outlet


class VisitService:
    """
    Visit management service.
    """

    # =====================================================
    # Retrieval
    # =====================================================

    @staticmethod
    def get_all(company_id):
        """
        Returns all company visits.
        """

        return Visit.query.filter_by(
            company_id=company_id,
            is_deleted=False
        ).order_by(
            Visit.visit_date.desc()
        ).all()

    @staticmethod
    def get_by_id(visit_id):
        """
        Returns a visit by ID.
        """

        return Visit.query.filter_by(
            id=visit_id,
            is_deleted=False
        ).first()

    @staticmethod
    def get_by_fsr(company_id, fsr_id):
        """
        Returns visits belonging to an FSR.
        """

        return Visit.query.filter_by(
            company_id=company_id,
            fsr_id=fsr_id,
            is_deleted=False
        ).order_by(
            Visit.visit_date.desc()
        ).all()

    @staticmethod
    def get_by_route(company_id, route_id):
        """
        Returns visits for a route.
        """

        return Visit.query.filter_by(
            company_id=company_id,
            route_id=route_id,
            is_deleted=False
        ).order_by(
            Visit.visit_date.desc()
        ).all()

    @staticmethod
    def get_by_outlet(company_id, outlet_id):
        """
        Returns visits for an outlet.
        """

        return Visit.query.filter_by(
            company_id=company_id,
            outlet_id=outlet_id,
            is_deleted=False
        ).order_by(
            Visit.visit_date.desc()
        ).all()

    # =====================================================
    # Create Visit
    # =====================================================

    @staticmethod
    def create(data):
        """
        Creates a visit.
        """

        visit = Visit(

            company_id=data.get("company_id"),

            outlet_id=data.get("outlet_id"),

            fsr_id=data.get("fsr_id"),

            distributor_id=data.get("distributor_id"),

            route_id=data.get("route_id"),

            visit_date=data.get("visit_date"),

            check_in_time=data.get(
                "check_in_time",
                datetime.utcnow()
            ),

            check_in_latitude=data.get(
                "check_in_latitude"
            ),

            check_in_longitude=data.get(
                "check_in_longitude"
            ),

            customer_feedback=data.get(
                "customer_feedback"
            ),

            competitor_activity=data.get(
                "competitor_activity"
            ),

            stock_observation=data.get(
                "stock_observation"
            ),

            notes=data.get("notes")

        )

        db.session.add(visit)

        outlet = Outlet.query.get(
            visit.outlet_id
        )

        if outlet:

            outlet.last_visit_date = visit.visit_date

        db.session.commit()

        return visit

    # =====================================================
    # Check Out
    # =====================================================

    @staticmethod
    def checkout(
        visit,
        latitude=None,
        longitude=None
    ):
        """
        Completes a visit.
        """

        checkout_time = datetime.utcnow()

        visit.check_out_time = checkout_time

        visit.check_out_latitude = latitude

        visit.check_out_longitude = longitude

        visit.visit_status = "Completed"

        duration = checkout_time - visit.check_in_time

        visit.visit_duration = int(
            duration.total_seconds() / 60
        )

        db.session.commit()

        return visit

    # =====================================================
    # Visit Notes
    # =====================================================

    @staticmethod
    def add_note(data):
        """
        Adds a visit note.
        """

        note = VisitNote(

            company_id=data.get("company_id"),

            visit_id=data.get("visit_id"),

            fsr_id=data.get("fsr_id"),

            title=data.get("title"),

            note=data.get("note"),

            note_type=data.get(
                "note_type",
                "General"
            ),

            requires_follow_up=data.get(
                "requires_follow_up",
                False
            ),

            follow_up_date=data.get(
                "follow_up_date"
            )

        )

        db.session.add(note)

        db.session.commit()

        return note

    @staticmethod
    def get_notes(visit_id):
        """
        Returns notes for a visit.
        """

        return VisitNote.query.filter_by(

            visit_id=visit_id,

            is_deleted=False

        ).order_by(

            VisitNote.created_at.desc()

        ).all()

    # =====================================================
    # Update
    # =====================================================

    @staticmethod
    def update(
        visit,
        data
    ):
        """
        Updates a visit.
        """

        for field, value in data.items():

            if hasattr(
                visit,
                field
            ):

                setattr(
                    visit,
                    field,
                    value
                )

        db.session.commit()

        return visit

    # =====================================================
    # Status
    # =====================================================

    @staticmethod
    def cancel(visit):
        """
        Cancels a visit.
        """

        visit.visit_status = "Cancelled"

        db.session.commit()

        return visit

    @staticmethod
    def delete(visit):
        """
        Soft deletes a visit.
        """

        visit.soft_delete()

    # =====================================================
    # Statistics
    # =====================================================

    @staticmethod
    def total(company_id):

        return Visit.query.filter_by(

            company_id=company_id,

            is_deleted=False

        ).count()

    @staticmethod
    def completed(company_id):

        return Visit.query.filter_by(

            company_id=company_id,

            visit_status="Completed",

            is_deleted=False

        ).count()

    @staticmethod
    def open(company_id):

        return Visit.query.filter_by(

            company_id=company_id,

            visit_status="Open",

            is_deleted=False

        ).count()

    @staticmethod
    def cancelled(company_id):

        return Visit.query.filter_by(

            company_id=company_id,

            visit_status="Cancelled",

            is_deleted=False

        ).count()