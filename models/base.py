import uuid

from datetime import datetime
from database.db import db


class BaseModel(db.Model):
    """
    Abstract base model inherited by all database models.

    Provides:
        - Primary Key
        - UUID
        - Active Status
        - Soft Delete
        - Created Timestamp
        - Updated Timestamp
    """

    __abstract__ = True

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    uuid = db.Column(
        db.String(36),
        unique=True,
        nullable=False,
        default=lambda: str(uuid.uuid4()),
        index=True
    )

    is_active = db.Column(
        db.Boolean,
        default=True,
        nullable=False
    )

    is_deleted = db.Column(
        db.Boolean,
        default=False,
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )

    def soft_delete(self):
        """
        Marks a record as deleted without removing it
        from the database.
        """
        self.is_deleted = True
        self.is_active = False

    def restore(self):
        """
        Restores a previously soft-deleted record.
        """
        self.is_deleted = False
        self.is_active = True

    def to_dict(self):
        """
        Converts model attributes into a dictionary.
        Excludes SQLAlchemy internal attributes.
        """
        return {
            column.name: getattr(self, column.name)
            for column in self.__table__.columns
        }

    def save(self):
        """
        Saves the current object.
        """
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """
        Permanently removes the object from the database.
        Use with caution.
        """
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.id}>"