"""
Outlet Service

Handles business logic related to
retail outlets.
"""

from sqlalchemy import or_

from database.db import db
from models import Outlet


class OutletService:
    """
    Outlet management service.
    """

    # =====================================================
    # Retrieval
    # =====================================================

    @staticmethod
    def get_all(company_id):
        """
        Returns all company outlets.
        """

        return Outlet.query.filter_by(
            company_id=company_id,
            is_deleted=False
        ).order_by(
            Outlet.name.asc()
        ).all()

    @staticmethod
    def get_by_id(outlet_id):
        """
        Returns an outlet by ID.
        """

        return Outlet.query.filter_by(
            id=outlet_id,
            is_deleted=False
        ).first()

    @staticmethod
    def get_by_code(company_id, outlet_code):
        """
        Returns an outlet by code.
        """

        return Outlet.query.filter_by(
            company_id=company_id,
            outlet_code=outlet_code,
            is_deleted=False
        ).first()

    @staticmethod
    def get_by_route(company_id, route_id):
        """
        Returns outlets assigned
        to a route.
        """

        return Outlet.query.filter_by(
            company_id=company_id,
            route_id=route_id,
            is_deleted=False
        ).order_by(
            Outlet.name.asc()
        ).all()

    @staticmethod
    def get_by_distributor(company_id, distributor_id):
        """
        Returns outlets assigned
        to a distributor.
        """

        return Outlet.query.filter_by(
            company_id=company_id,
            distributor_id=distributor_id,
            is_deleted=False
        ).order_by(
            Outlet.name.asc()
        ).all()

    @staticmethod
    def get_by_fsr(company_id, fsr_id):
        """
        Returns outlets assigned
        to an FSR.
        """

        return Outlet.query.filter_by(
            company_id=company_id,
            fsr_id=fsr_id,
            is_deleted=False
        ).order_by(
            Outlet.name.asc()
        ).all()

    @staticmethod
    def search(company_id, search_term):
        """
        Searches outlets.
        """

        return Outlet.query.filter(

            Outlet.company_id == company_id,

            Outlet.is_deleted == False,

            or_(

                Outlet.name.ilike(
                    f"%{search_term}%"
                ),

                Outlet.outlet_code.ilike(
                    f"%{search_term}%"
                ),

                Outlet.owner_name.ilike(
                    f"%{search_term}%"
                ),

                Outlet.phone.ilike(
                    f"%{search_term}%"
                ),

                Outlet.town.ilike(
                    f"%{search_term}%"
                )

            )

        ).order_by(

            Outlet.name.asc()

        ).all()

    # =====================================================
    # Create
    # =====================================================

    @staticmethod
    def create(data):
        """
        Creates a new outlet.
        """

        outlet = Outlet(

            company_id=data.get("company_id"),

            outlet_category_id=data.get(
                "outlet_category_id"
            ),

            territory_id=data.get(
                "territory_id"
            ),

            route_id=data.get(
                "route_id"
            ),

            distributor_id=data.get(
                "distributor_id"
            ),

            fsr_id=data.get(
                "fsr_id"
            ),

            name=data.get("name"),

            outlet_code=data.get(
                "outlet_code"
            ),

            description=data.get(
                "description"
            ),

            owner_name=data.get(
                "owner_name"
            ),

            owner_phone=data.get(
                "owner_phone"
            ),

            owner_email=data.get(
                "owner_email"
            ),

            phone=data.get("phone"),

            alternative_phone=data.get(
                "alternative_phone"
            ),

            email=data.get("email"),

            address=data.get(
                "address"
            ),

            town=data.get("town"),

            county=data.get("county"),

            landmark=data.get(
                "landmark"
            ),

            latitude=data.get(
                "latitude"
            ),

            longitude=data.get(
                "longitude"
            ),

            business_since=data.get(
                "business_since"
            ),

            average_monthly_sales=data.get(
                "average_monthly_sales"
            ),

            credit_limit=data.get(
                "credit_limit",
                0.00
            ),

            opening_balance=data.get(
                "opening_balance",
                0.00
            ),

            preferred_visit_day=data.get(
                "preferred_visit_day"
            ),

            notes=data.get("notes")

        )

        db.session.add(outlet)
        db.session.commit()

        return outlet

    # =====================================================
    # Update
    # =====================================================

    @staticmethod
    def update(outlet, data):
        """
        Updates an outlet.
        """

        for field, value in data.items():

            if hasattr(outlet, field):

                setattr(
                    outlet,
                    field,
                    value
                )

        db.session.commit()

        return outlet

    # =====================================================
    # Visit Tracking
    # =====================================================

    @staticmethod
    def update_last_visit(
        outlet,
        visit_date
    ):
        """
        Updates the last visit date.
        """

        outlet.last_visit_date = visit_date

        db.session.commit()

    @staticmethod
    def update_last_order(
        outlet,
        order_date
    ):
        """
        Updates the last order date.
        """

        outlet.last_order_date = order_date

        db.session.commit()

    # =====================================================
    # Status
    # =====================================================

    @staticmethod
    def activate(outlet):

        outlet.outlet_status = "Active"
        outlet.is_active = True

        db.session.commit()

        return outlet

    @staticmethod
    def deactivate(outlet):

        outlet.outlet_status = "Inactive"
        outlet.is_active = False

        db.session.commit()

        return outlet

    @staticmethod
    def close(outlet):

        outlet.outlet_status = "Closed"

        db.session.commit()

        return outlet

    @staticmethod
    def delete(outlet):

        outlet.soft_delete()

    # =====================================================
    # Statistics
    # =====================================================

    @staticmethod
    def total(company_id):

        return Outlet.query.filter_by(
            company_id=company_id,
            is_deleted=False
        ).count()

    @staticmethod
    def active(company_id):

        return Outlet.query.filter_by(
            company_id=company_id,
            outlet_status="Active",
            is_deleted=False
        ).count()

    @staticmethod
    def inactive(company_id):

        return Outlet.query.filter_by(
            company_id=company_id,
            outlet_status="Inactive",
            is_deleted=False
        ).count()

    @staticmethod
    def closed(company_id):

        return Outlet.query.filter_by(
            company_id=company_id,
            outlet_status="Closed",
            is_deleted=False
        ).count()