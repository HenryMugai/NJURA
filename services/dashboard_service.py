"""
Dashboard Service

Handles dashboard metrics and widgets
for the N.J.U.R.A platform.
"""

from sqlalchemy import func

from models import (
    Dashboard,
    Delivery,
    Distributor,
    FSR,
    Order,
    Outlet,
    Product,
    Visit
)

from database.db import db


class DashboardService:
    """
    Dashboard service.
    """

    # =====================================================
    # Dashboard
    # =====================================================

    @staticmethod
    def get_dashboard(user_id, company_id):
        """
        Returns a user's dashboard.
        """

        dashboard = Dashboard.query.filter_by(

            user_id=user_id,

            company_id=company_id,

            is_deleted=False

        ).first()

        if dashboard:

            return dashboard

        dashboard = Dashboard(

            user_id=user_id,

            company_id=company_id

        )

        db.session.add(dashboard)
        db.session.commit()

        return dashboard

    # =====================================================
    # Dashboard Summary
    # =====================================================

    @staticmethod
    def summary(company_id):
        """
        Returns dashboard KPIs.
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

            "visits": Visit.query.filter_by(
                company_id=company_id,
                is_deleted=False
            ).count(),

            "orders": Order.query.filter_by(
                company_id=company_id,
                is_deleted=False
            ).count(),

            "deliveries": Delivery.query.filter_by(
                company_id=company_id,
                is_deleted=False
            ).count(),

            "sales": db.session.query(
                func.sum(Order.total_amount)
            ).filter(
                Order.company_id == company_id,
                Order.is_deleted == False
            ).scalar() or 0

        }

    # =====================================================
    # Recent Orders
    # =====================================================

    @staticmethod
    def recent_orders(
        company_id,
        limit=10
    ):
        """
        Returns recent orders.
        """

        return Order.query.filter_by(

            company_id=company_id,

            is_deleted=False

        ).order_by(

            Order.order_date.desc()

        ).limit(limit).all()

    # =====================================================
    # Recent Visits
    # =====================================================

    @staticmethod
    def recent_visits(
        company_id,
        limit=10
    ):
        """
        Returns recent visits.
        """

        return Visit.query.filter_by(

            company_id=company_id,

            is_deleted=False

        ).order_by(

            Visit.visit_date.desc()

        ).limit(limit).all()

    # =====================================================
    # Recent Deliveries
    # =====================================================

    @staticmethod
    def recent_deliveries(
        company_id,
        limit=10
    ):
        """
        Returns recent deliveries.
        """

        return Delivery.query.filter_by(

            company_id=company_id,

            is_deleted=False

        ).order_by(

            Delivery.created_at.desc()

        ).limit(limit).all()

    # =====================================================
    # Dashboard Preferences
    # =====================================================

    @staticmethod
    def update_layout(
        dashboard,
        layout
    ):
        """
        Updates dashboard layout.
        """

        dashboard.layout = layout

        db.session.commit()

        return dashboard

    @staticmethod
    def update_widgets(
        dashboard,
        widgets
    ):
        """
        Updates dashboard widgets.
        """

        dashboard.widgets = widgets

        db.session.commit()

        return dashboard

    @staticmethod
    def update_filters(
        dashboard,
        filters
    ):
        """
        Updates dashboard filters.
        """

        dashboard.filters = filters

        db.session.commit()

        return dashboard

    @staticmethod
    def update_refresh_interval(
        dashboard,
        interval
    ):
        """
        Updates auto refresh interval.
        """

        dashboard.refresh_interval = interval

        db.session.commit()

        return dashboard

    # =====================================================
    # Dashboard Statistics
    # =====================================================

    @staticmethod
    def orders_by_status(company_id):
        """
        Returns order status counts.
        """

        return db.session.query(

            Order.order_status,

            func.count(Order.id)

        ).filter(

            Order.company_id == company_id,

            Order.is_deleted == False

        ).group_by(

            Order.order_status

        ).all()

    @staticmethod
    def deliveries_by_status(company_id):
        """
        Returns delivery status counts.
        """

        return db.session.query(

            Delivery.delivery_status,

            func.count(Delivery.id)

        ).filter(

            Delivery.company_id == company_id,

            Delivery.is_deleted == False

        ).group_by(

            Delivery.delivery_status

        ).all()

    @staticmethod
    def visits_by_status(company_id):
        """
        Returns visit status counts.
        """

        return db.session.query(

            Visit.visit_status,

            func.count(Visit.id)

        ).filter(

            Visit.company_id == company_id,

            Visit.is_deleted == False

        ).group_by(

            Visit.visit_status

        ).all()