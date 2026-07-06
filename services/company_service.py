"""
Company Service

Handles all business logic related to
company management.
"""

from sqlalchemy import or_

from database.db import db
from models import Company


class CompanyService:
    """
    Company management service.
    """

    # =====================================================
    # Retrieval
    # =====================================================

    @staticmethod
    def get_all():
        """
        Returns all active companies.
        """

        return Company.query.filter_by(
            is_deleted=False
        ).order_by(
            Company.name.asc()
        ).all()

    @staticmethod
    def get_by_id(company_id):
        """
        Returns a company by ID.
        """

        return Company.query.filter_by(
            id=company_id,
            is_deleted=False
        ).first()

    @staticmethod
    def get_by_slug(slug):
        """
        Returns a company by slug.
        """

        return Company.query.filter_by(
            slug=slug,
            is_deleted=False
        ).first()

    @staticmethod
    def get_by_code(company_code):
        """
        Returns a company using its code.
        """

        return Company.query.filter_by(
            company_code=company_code,
            is_deleted=False
        ).first()

    @staticmethod
    def search(search_term):
        """
        Searches companies.
        """

        return Company.query.filter(

            Company.is_deleted == False,

            or_(

                Company.name.ilike(f"%{search_term}%"),

                Company.company_code.ilike(f"%{search_term}%"),

                Company.email.ilike(f"%{search_term}%"),

                Company.phone.ilike(f"%{search_term}%")

            )

        ).order_by(

            Company.name.asc()

        ).all()

    # =====================================================
    # Create
    # =====================================================

    @staticmethod
    def create(data):
        """
        Creates a new company.
        """

        company = Company(

            name=data.get("name"),

            company_code=data.get("company_code"),

            slug=data.get("slug"),

            description=data.get("description"),

            industry=data.get("industry"),

            initials=data.get("initials"),

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

            registration_number=data.get(
                "registration_number"
            ),

            kra_pin=data.get("kra_pin"),

            logo_url=data.get("logo_url"),

            brand_primary_color=data.get(
                "brand_primary_color"
            ),

            brand_secondary_color=data.get(
                "brand_secondary_color"
            ),

            address=data.get("address"),

            town=data.get("town"),

            county=data.get("county"),

            country=data.get(
                "country",
                "Kenya"
            ),

            postal_address=data.get(
                "postal_address"
            ),

            postal_code=data.get(
                "postal_code"
            ),

            timezone=data.get(
                "timezone",
                "Africa/Nairobi"
            ),

            currency=data.get(
                "currency",
                "KES"
            ),

            date_format=data.get(
                "date_format",
                "DD/MM/YYYY"
            ),

            allow_outlet_creation=data.get(
                "allow_outlet_creation",
                True
            ),

            allow_order_editing=data.get(
                "allow_order_editing",
                True
            ),

            require_visit_before_order=data.get(
                "require_visit_before_order",
                True
            ),

            company_status="Pending"

        )

        db.session.add(company)
        db.session.commit()

        return company

    # =====================================================
    # Update
    # =====================================================

    @staticmethod
    def update(company, data):
        """
        Updates a company.
        """

        for field, value in data.items():

            if hasattr(company, field):

                setattr(
                    company,
                    field,
                    value
                )

        db.session.commit()

        return company

    # =====================================================
    # Status
    # =====================================================

    @staticmethod
    def activate(company):
        """
        Activates a company.
        """

        company.company_status = "Active"
        company.is_active = True

        db.session.commit()

        return company

    @staticmethod
    def suspend(company):
        """
        Suspends a company.
        """

        company.company_status = "Suspended"

        db.session.commit()

        return company

    @staticmethod
    def archive(company):
        """
        Archives a company.
        """

        company.company_status = "Archived"

        db.session.commit()

        return company

    @staticmethod
    def verify(company):
        """
        Marks a company as verified.
        """

        company.is_verified = True

        db.session.commit()

        return company

    @staticmethod
    def complete_onboarding(company):
        """
        Marks onboarding as completed.
        """

        company.onboarding_completed = True

        db.session.commit()

        return company

    # =====================================================
    # Delete
    # =====================================================

    @staticmethod
    def delete(company):
        """
        Soft deletes a company.
        """

        company.soft_delete()

    # =====================================================
    # Statistics
    # =====================================================

    @staticmethod
    def total_companies():
        """
        Returns total active companies.
        """

        return Company.query.filter_by(
            is_deleted=False
        ).count()

    @staticmethod
    def active_companies():
        """
        Returns total active companies.
        """

        return Company.query.filter_by(
            company_status="Active",
            is_deleted=False
        ).count()

    @staticmethod
    def pending_companies():
        """
        Returns pending companies.
        """

        return Company.query.filter_by(
            company_status="Pending",
            is_deleted=False
        ).count()

    @staticmethod
    def suspended_companies():
        """
        Returns suspended companies.
        """

        return Company.query.filter_by(
            company_status="Suspended",
            is_deleted=False
        ).count()