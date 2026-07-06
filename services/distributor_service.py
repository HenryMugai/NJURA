"""
Distributor Service

Handles business logic related to
company distributors.
"""

from sqlalchemy import or_

from database.db import db
from models import Distributor


class DistributorService:
    """
    Distributor management service.
    """

    # =====================================================
    # Retrieval
    # =====================================================

    @staticmethod
    def get_all(company_id):
        """
        Returns all distributors
        belonging to a company.
        """

        return Distributor.query.filter_by(
            company_id=company_id,
            is_deleted=False
        ).order_by(
            Distributor.name.asc()
        ).all()

    @staticmethod
    def get_by_id(distributor_id):
        """
        Returns a distributor by ID.
        """

        return Distributor.query.filter_by(
            id=distributor_id,
            is_deleted=False
        ).first()

    @staticmethod
    def get_by_code(company_id, distributor_code):
        """
        Returns distributor using code.
        """

        return Distributor.query.filter_by(
            company_id=company_id,
            distributor_code=distributor_code,
            is_deleted=False
        ).first()

    @staticmethod
    def get_by_territory(company_id, territory_id):
        """
        Returns distributors assigned
        to a territory.
        """

        return Distributor.query.filter_by(
            company_id=company_id,
            territory_id=territory_id,
            is_deleted=False
        ).order_by(
            Distributor.name.asc()
        ).all()

    @staticmethod
    def search(company_id, search_term):
        """
        Searches distributors.
        """

        return Distributor.query.filter(

            Distributor.company_id == company_id,

            Distributor.is_deleted == False,

            or_(

                Distributor.name.ilike(
                    f"%{search_term}%"
                ),

                Distributor.distributor_code.ilike(
                    f"%{search_term}%"
                ),

                Distributor.phone.ilike(
                    f"%{search_term}%"
                ),

                Distributor.email.ilike(
                    f"%{search_term}%"
                ),

                Distributor.contact_person.ilike(
                    f"%{search_term}%"
                )

            )

        ).order_by(

            Distributor.name.asc()

        ).all()

    # =====================================================
    # Create
    # =====================================================

    @staticmethod
    def create(data):
        """
        Creates a distributor.
        """

        distributor = Distributor(

            company_id=data.get("company_id"),

            territory_id=data.get("territory_id"),

            name=data.get("name"),

            distributor_code=data.get(
                "distributor_code"
            ),

            description=data.get(
                "description"
            ),

            kra_pin=data.get("kra_pin"),

            registration_number=data.get(
                "registration_number"
            ),

            email=data.get("email"),

            phone=data.get("phone"),

            alternative_phone=data.get(
                "alternative_phone"
            ),

            website=data.get("website"),

            contact_person=data.get(
                "contact_person"
            ),

            contact_person_phone=data.get(
                "contact_person_phone"
            ),

            contact_person_email=data.get(
                "contact_person_email"
            ),

            address=data.get("address"),

            town=data.get("town"),

            county=data.get("county"),

            postal_address=data.get(
                "postal_address"
            ),

            postal_code=data.get(
                "postal_code"
            ),

            notes=data.get("notes")

        )

        db.session.add(distributor)
        db.session.commit()

        return distributor

    # =====================================================
    # Update
    # =====================================================

    @staticmethod
    def update(distributor, data):
        """
        Updates distributor information.
        """

        for field, value in data.items():

            if hasattr(distributor, field):

                setattr(
                    distributor,
                    field,
                    value
                )

        db.session.commit()

        return distributor

    # =====================================================
    # Status
    # =====================================================

    @staticmethod
    def activate(distributor):
        """
        Activates a distributor.
        """

        distributor.distributor_status = "Active"
        distributor.is_active = True

        db.session.commit()

        return distributor

    @staticmethod
    def suspend(distributor):
        """
        Suspends a distributor.
        """

        distributor.distributor_status = "Suspended"

        db.session.commit()

        return distributor

    @staticmethod
    def deactivate(distributor):
        """
        Deactivates a distributor.
        """

        distributor.distributor_status = "Inactive"
        distributor.is_active = False

        db.session.commit()

        return distributor

    # =====================================================
    # Delete
    # =====================================================

    @staticmethod
    def delete(distributor):
        """
        Soft deletes a distributor.
        """

        distributor.soft_delete()

    # =====================================================
    # Statistics
    # =====================================================

    @staticmethod
    def total(company_id):
        """
        Returns total distributors.
        """

        return Distributor.query.filter_by(
            company_id=company_id,
            is_deleted=False
        ).count()

    @staticmethod
    def active(company_id):
        """
        Returns active distributors.
        """

        return Distributor.query.filter_by(
            company_id=company_id,
            distributor_status="Active",
            is_deleted=False
        ).count()

    @staticmethod
    def inactive(company_id):
        """
        Returns inactive distributors.
        """

        return Distributor.query.filter_by(
            company_id=company_id,
            distributor_status="Inactive",
            is_deleted=False
        ).count()

    @staticmethod
    def suspended(company_id):
        """
        Returns suspended distributors.
        """

        return Distributor.query.filter_by(
            company_id=company_id,
            distributor_status="Suspended",
            is_deleted=False
        ).count()