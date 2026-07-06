"""
Notification Service

Handles creation, delivery and management
of system notifications.
"""

from datetime import datetime

from database.db import db
from models import Notification


class NotificationService:
    """
    Notification management service.
    """

    # =====================================================
    # Retrieval
    # =====================================================

    @staticmethod
    def get_all(user_id):
        """
        Returns all notifications
        for a user.
        """

        return Notification.query.filter_by(
            user_id=user_id,
            is_deleted=False
        ).order_by(
            Notification.created_at.desc()
        ).all()

    @staticmethod
    def get_unread(user_id):
        """
        Returns unread notifications.
        """

        return Notification.query.filter_by(
            user_id=user_id,
            is_read=False,
            is_deleted=False
        ).order_by(
            Notification.created_at.desc()
        ).all()

    @staticmethod
    def get_by_id(notification_id):
        """
        Returns a notification.
        """

        return Notification.query.filter_by(
            id=notification_id,
            is_deleted=False
        ).first()

    # =====================================================
    # Create
    # =====================================================

    @staticmethod
    def create(data):
        """
        Creates a notification.
        """

        notification = Notification(

            company_id=data.get("company_id"),

            user_id=data.get("user_id"),

            title=data.get("title"),

            message=data.get("message"),

            notification_type=data.get(
                "notification_type",
                "System"
            ),

            delivery_channel=data.get(
                "delivery_channel",
                "In-App"
            ),

            action_url=data.get(
                "action_url"
            ),

            reference_type=data.get(
                "reference_type"
            ),

            reference_id=data.get(
                "reference_id"
            ),

            scheduled_at=data.get(
                "scheduled_at"
            ),

            notes=data.get(
                "notes"
            )

        )

        db.session.add(notification)
        db.session.commit()

        return notification

    # =====================================================
    # Update
    # =====================================================

    @staticmethod
    def update(notification, data):
        """
        Updates a notification.
        """

        for field, value in data.items():

            if hasattr(notification, field):

                setattr(
                    notification,
                    field,
                    value
                )

        db.session.commit()

        return notification

    # =====================================================
    # Status Management
    # =====================================================

    @staticmethod
    def mark_as_sent(notification):
        """
        Marks notification as sent.
        """

        notification.notification_status = "Sent"

        notification.sent_at = datetime.utcnow()

        db.session.commit()

        return notification

    @staticmethod
    def mark_as_delivered(notification):
        """
        Marks notification as delivered.
        """

        notification.notification_status = "Delivered"

        db.session.commit()

        return notification

    @staticmethod
    def mark_as_read(notification):
        """
        Marks notification as read.
        """

        notification.notification_status = "Read"

        notification.is_read = True

        notification.read_at = datetime.utcnow()

        db.session.commit()

        return notification

    @staticmethod
    def mark_as_failed(notification):
        """
        Marks notification as failed.
        """

        notification.notification_status = "Failed"

        db.session.commit()

        return notification

    # =====================================================
    # Bulk Actions
    # =====================================================

    @staticmethod
    def mark_all_as_read(user_id):
        """
        Marks all notifications as read.
        """

        notifications = Notification.query.filter_by(

            user_id=user_id,

            is_read=False,

            is_deleted=False

        ).all()

        for notification in notifications:

            notification.is_read = True

            notification.notification_status = "Read"

            notification.read_at = datetime.utcnow()

        db.session.commit()

        return len(notifications)

    # =====================================================
    # Delete
    # =====================================================

    @staticmethod
    def delete(notification):
        """
        Soft deletes a notification.
        """

        notification.soft_delete()

    # =====================================================
    # Statistics
    # =====================================================

    @staticmethod
    def total(user_id):
        """
        Returns total notifications.
        """

        return Notification.query.filter_by(

            user_id=user_id,

            is_deleted=False

        ).count()

    @staticmethod
    def unread(user_id):
        """
        Returns unread notifications.
        """

        return Notification.query.filter_by(

            user_id=user_id,

            is_read=False,

            is_deleted=False

        ).count()

    @staticmethod
    def read(user_id):
        """
        Returns read notifications.
        """

        return Notification.query.filter_by(

            user_id=user_id,

            is_read=True,

            is_deleted=False

        ).count()

    @staticmethod
    def pending(user_id):
        """
        Returns pending notifications.
        """

        return Notification.query.filter_by(

            user_id=user_id,

            notification_status="Pending",

            is_deleted=False

        ).count()