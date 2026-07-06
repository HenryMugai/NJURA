"""
Order Service

Handles business logic related to
customer orders.
"""

from datetime import datetime

from database.db import db
from models import (
    Order,
    OrderItem,
    Outlet
)


class OrderService:
    """
    Order management service.
    """

    # =====================================================
    # Retrieval
    # =====================================================

    @staticmethod
    def get_all(company_id):
        """
        Returns all company orders.
        """

        return Order.query.filter_by(
            company_id=company_id,
            is_deleted=False
        ).order_by(
            Order.order_date.desc()
        ).all()

    @staticmethod
    def get_by_id(order_id):
        """
        Returns an order by ID.
        """

        return Order.query.filter_by(
            id=order_id,
            is_deleted=False
        ).first()

    @staticmethod
    def get_by_number(
        company_id,
        order_number
    ):
        """
        Returns an order using
        its order number.
        """

        return Order.query.filter_by(
            company_id=company_id,
            order_number=order_number,
            is_deleted=False
        ).first()

    @staticmethod
    def get_by_fsr(
        company_id,
        fsr_id
    ):
        """
        Returns all orders
        created by an FSR.
        """

        return Order.query.filter_by(
            company_id=company_id,
            fsr_id=fsr_id,
            is_deleted=False
        ).order_by(
            Order.order_date.desc()
        ).all()

    @staticmethod
    def get_by_distributor(
        company_id,
        distributor_id
    ):
        """
        Returns distributor orders.
        """

        return Order.query.filter_by(
            company_id=company_id,
            distributor_id=distributor_id,
            is_deleted=False
        ).order_by(
            Order.order_date.desc()
        ).all()

    @staticmethod
    def get_by_outlet(
        company_id,
        outlet_id
    ):
        """
        Returns outlet orders.
        """

        return Order.query.filter_by(
            company_id=company_id,
            outlet_id=outlet_id,
            is_deleted=False
        ).order_by(
            Order.order_date.desc()
        ).all()

    # =====================================================
    # Create Order
    # =====================================================

    @staticmethod
    def create(data):
        """
        Creates a customer order.
        """

        order = Order(

            company_id=data.get("company_id"),

            outlet_id=data.get("outlet_id"),

            visit_id=data.get("visit_id"),

            distributor_id=data.get(
                "distributor_id"
            ),

            fsr_id=data.get("fsr_id"),

            route_id=data.get("route_id"),

            order_number=data.get(
                "order_number"
            ),

            order_date=data.get(
                "order_date",
                datetime.utcnow()
            ),

            requested_delivery_date=data.get(
                "requested_delivery_date"
            ),

            order_type=data.get(
                "order_type",
                "Sale"
            ),

            order_source=data.get(
                "order_source",
                "Mobile"
            ),

            subtotal=data.get(
                "subtotal",
                0.00
            ),

            discount_amount=data.get(
                "discount_amount",
                0.00
            ),

            tax_amount=data.get(
                "tax_amount",
                0.00
            ),

            total_amount=data.get(
                "total_amount",
                0.00
            ),

            remarks=data.get("remarks")

        )

        db.session.add(order)

        outlet = Outlet.query.get(
            order.outlet_id
        )

        if outlet:

            outlet.last_order_date = (
                order.order_date.date()
            )

        db.session.commit()

        return order

    # =====================================================
    # Order Items
    # =====================================================

    @staticmethod
    def add_item(data):
        """
        Adds an item to an order.
        """

        item = OrderItem(

            company_id=data.get("company_id"),

            order_id=data.get("order_id"),

            product_id=data.get("product_id"),

            product_price_id=data.get(
                "product_price_id"
            ),

            product_name=data.get(
                "product_name"
            ),

            sku=data.get("sku"),

            unit_of_measure=data.get(
                "unit_of_measure"
            ),

            quantity=data.get(
                "quantity",
                1
            ),

            free_quantity=data.get(
                "free_quantity",
                0
            ),

            unit_price=data.get(
                "unit_price",
                0.00
            ),

            discount_percentage=data.get(
                "discount_percentage",
                0.00
            ),

            discount_amount=data.get(
                "discount_amount",
                0.00
            ),

            tax_percentage=data.get(
                "tax_percentage",
                0.00
            ),

            tax_amount=data.get(
                "tax_amount",
                0.00
            ),

            line_total=data.get(
                "line_total",
                0.00
            ),

            notes=data.get("notes")

        )

        db.session.add(item)

        db.session.commit()

        return item

    @staticmethod
    def get_items(order_id):
        """
        Returns all order items.
        """

        return OrderItem.query.filter_by(

            order_id=order_id,

            is_deleted=False

        ).all()

    # =====================================================
    # Update
    # =====================================================

    @staticmethod
    def update(
        order,
        data
    ):
        """
        Updates an order.
        """

        for field, value in data.items():

            if hasattr(
                order,
                field
            ):

                setattr(
                    order,
                    field,
                    value
                )

        db.session.commit()

        return order

    # =====================================================
    # Status
    # =====================================================

    @staticmethod
    def approve(order):
        """
        Approves an order.
        """

        order.approval_status = "Approved"

        db.session.commit()

        return order

    @staticmethod
    def reject(order):
        """
        Rejects an order.
        """

        order.approval_status = "Rejected"

        db.session.commit()

        return order

    @staticmethod
    def dispatch(order):
        """
        Marks an order as dispatched.
        """

        order.order_status = "Dispatched"

        db.session.commit()

        return order

    @staticmethod
    def deliver(order):
        """
        Marks an order as delivered.
        """

        order.order_status = "Delivered"

        db.session.commit()

        return order

    @staticmethod
    def cancel(order):
        """
        Cancels an order.
        """

        order.order_status = "Cancelled"

        db.session.commit()

        return order

    @staticmethod
    def delete(order):
        """
        Soft deletes an order.
        """

        order.soft_delete()

    # =====================================================
    # Statistics
    # =====================================================

    @staticmethod
    def total(company_id):

        return Order.query.filter_by(
            company_id=company_id,
            is_deleted=False
        ).count()

    @staticmethod
    def pending(company_id):

        return Order.query.filter_by(
            company_id=company_id,
            approval_status="Pending",
            is_deleted=False
        ).count()

    @staticmethod
    def approved(company_id):

        return Order.query.filter_by(
            company_id=company_id,
            approval_status="Approved",
            is_deleted=False
        ).count()

    @staticmethod
    def delivered(company_id):

        return Order.query.filter_by(
            company_id=company_id,
            order_status="Delivered",
            is_deleted=False
        ).count()

    @staticmethod
    def cancelled(company_id):

        return Order.query.filter_by(
            company_id=company_id,
            order_status="Cancelled",
            is_deleted=False
        ).count()