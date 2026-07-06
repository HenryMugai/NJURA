import uuid
from datetime import datetime

from database.db import db


class BaseModel(db.Model):
    """
    Abstract base model inherited by all models.

    Provides:
        - Primary Key
        - UUID
        - Active Status
        - Soft Delete
        - Created Timestamp
        - Updated Timestamp
    """

    __abstract__ = True

    # =====================================================
    # Primary Key
    # =====================================================

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    uuid = db.Column(
        db.String(36),
        nullable=False,
        unique=True,
        default=lambda: str(uuid.uuid4()),
        index=True
    )

    # =====================================================
    # Record Status
    # =====================================================

    is_active = db.Column(
        db.Boolean,
        nullable=False,
        default=True
    )

    is_deleted = db.Column(
        db.Boolean,
        nullable=False,
        default=False
    )

    # =====================================================
    # Audit Information
    # =====================================================

    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    updated_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    # =====================================================
    # Helper Methods
    # =====================================================

    def save(self):
        """
        Save the current record.
        """
        db.session.add(self)
        db.session.commit()

    def soft_delete(self):
        """
        Soft delete the current record.
        """
        self.is_deleted = True
        self.is_active = False
        db.session.commit()

    def restore(self):
        """
        Restore a soft-deleted record.
        """
        self.is_deleted = False
        self.is_active = True
        db.session.commit()

    def hard_delete(self):
        """
        Permanently remove the record.
        """
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        """
        Convert the model into a dictionary.
        """
        return {
            column.name: getattr(self, column.name)
            for column in self.__table__.columns
        }

    # =====================================================
    # Object Representation
    # =====================================================

    def __repr__(self):
        return (
            f"<{self.__class__.__name__}(id={self.id})>"
        )