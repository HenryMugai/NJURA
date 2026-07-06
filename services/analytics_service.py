"""
Analytics Service

Provides advanced analytics and business
intelligence metrics for the N.J.U.R.A platform.
"""

from sqlalchemy import func

from database.db import db
from models import (
    Delivery,
    Distributor,
    FSR,
    Order,
    OrderItem,
    Outlet,
    Product,
    Visit
)


class AnalyticsService:
    """
    Analytics service.
    """

    # =====================================================
    # Sales Analytics
    # =====================================================

    @staticmethod
    def total_sales(company_id):
        """
        Returns total sales.
        """

        total = db.session.query(

            func.sum(Order.total_amount)

        ).filter(

            Order.company_id == company_id,

            Order.is_deleted == False

        ).scalar()

        return total or 0

    @staticmethod
    def average_order_value(company_id):
        """
        Returns average order value.
        """

        average = db.session.query(

            func.avg(Order.total_amount)

        ).filter(

            Order.company_id == company_id,

            Order.is_deleted == False

        ).scalar()

        return average or 0

    @staticmethod
    def total_orders(company_id):
        """
        Returns total orders.
        """

        return Order.query.filter_by(

            company_id=company_id,

            is_deleted=False

        ).count()

    # =====================================================
    # Visit Analytics
    # =====================================================

    @staticmethod
    def total_visits(company_id):
        """
        Returns total visits.
        """

        return Visit.query.filter_by(

            company_id=company_id,

            is_deleted=False

        ).count()

    @staticmethod
    def average_visit_duration(company_id):
        """
        Returns average visit duration.
        """

        duration = db.session.query(

            func.avg(Visit.visit_duration)

        ).filter(

            Visit.company_id == company_id,

            Visit.is_deleted == False,

            Visit.visit_duration.isnot(None)

        ).scalar()

        return duration or 0

    # =====================================================
    # Product Analytics
    # =====================================================

    @staticmethod
    def top_selling_products(
        company_id,
        limit=10
    ):
        """
        Returns top selling products.
        """

        return db.session.query(

            Product,

            func.sum(
                OrderItem.quantity
            ).label("quantity_sold")

        ).join(

            OrderItem,

            Product.id == OrderItem.product_id

        ).filter(

            Product.company_id == company_id,

            Product.is_deleted == False,

            OrderItem.is_deleted == False

        ).group_by(

            Product.id

        ).order_by(

            func.sum(
                OrderItem.quantity
            ).desc()

        ).limit(limit).all()

    # =====================================================
    # Outlet Analytics
    # =====================================================

    @staticmethod
    def most_active_outlets(
        company_id,
        limit=10
    ):
        """
        Returns outlets with the
        highest number of visits.
        """

        return db.session.query(

            Outlet,

            func.count(
                Visit.id
            ).label("visit_count")

        ).join(

            Visit,

            Outlet.id == Visit.outlet_id

        ).filter(

            Outlet.company_id == company_id,

            Outlet.is_deleted == False,

            Visit.is_deleted == False

        ).group_by(

            Outlet.id

        ).order_by(

            func.count(
                Visit.id
            ).desc()

        ).limit(limit).all()

    # =====================================================
    # FSR Analytics
    # =====================================================

    @staticmethod
    def top_fsrs(
        company_id,
        limit=10
    ):
        """
        Returns top performing FSRs
        based on orders created.
        """

        return db.session.query(

            FSR,

            func.count(
                Order.id
            ).label("orders_created")

        ).join(

            Order,

            FSR.id == Order.fsr_id

        ).filter(

            FSR.company_id == company_id,

            FSR.is_deleted == False,

            Order.is_deleted == False

        ).group_by(

            FSR.id

        ).order_by(

            func.count(
                Order.id
            ).desc()

        ).limit(limit).all()

    # =====================================================
    # Distributor Analytics
    # =====================================================

    @staticmethod
    def top_distributors(
        company_id,
        limit=10
    ):
        """
        Returns top distributors
        based on fulfilled orders.
        """

        return db.session.query(

            Distributor,

            func.count(
                Delivery.id
            ).label("deliveries")

        ).join(

            Delivery,

            Distributor.id == Delivery.distributor_id

        ).filter(

            Distributor.company_id == company_id,

            Distributor.is_deleted == False,

            Delivery.is_deleted == False

        ).group_by(

            Distributor.id

        ).order_by(

            func.count(
                Delivery.id
            ).desc()

        ).limit(limit).all()

    # =====================================================
    # Delivery Analytics
    # =====================================================

    @staticmethod
    def delivery_success_rate(company_id):
        """
        Returns delivery success rate.
        """

        total = Delivery.query.filter_by(

            company_id=company_id,

            is_deleted=False

        ).count()

        if total == 0:

            return 0

        delivered = Delivery.query.filter_by(

            company_id=company_id,

            delivery_status="Delivered",

            is_deleted=False

        ).count()

        return round(
            (delivered / total) * 100,
            2
        )

    # =====================================================
    # Business Growth
    # =====================================================

    @staticmethod
    def company_snapshot(company_id):
        """
        Returns key business metrics.
        """

        return {

            "products": Product.query.filter_by(
                company_id=company_id,
                is_deleted=False
            ).count(),

            "outlets": Outlet.query.filter_by(
                company_id=company_id,
                is_deleted=False
            ).count(),

            "fsrs": FSR.query.filter_by(
                company_id=company_id,
                is_deleted=False
            ).count(),

            "distributors": Distributor.query.filter_by(
                company_id=company_id,
                is_deleted=False
            ).count(),

            "orders": Order.query.filter_by(
                company_id=company_id,
                is_deleted=False
            ).count(),

            "visits": Visit.query.filter_by(
                company_id=company_id,
                is_deleted=False
            ).count(),

            "sales": AnalyticsService.total_sales(
                company_id
            ),

            "average_order_value":
                AnalyticsService.average_order_value(
                    company_id
                ),

            "delivery_success_rate":
                AnalyticsService.delivery_success_rate(
                    company_id
                )

        }