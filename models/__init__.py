"""
N.J.U.R.A Database Models

This package contains all SQLAlchemy models used
throughout the application.

NOTE:
The import order below is intentional to ensure all
SQLAlchemy relationships are available before the
application initializes the ORM.
"""

# =====================================================
# Base Model
# =====================================================

from .base import BaseModel

# =====================================================
# Core System Models
# =====================================================

from .company import Company
from .subscription import Subscription

from .role import Role
from .permission import Permission
from .role_permission import RolePermission

from .user import User

# =====================================================
# Sales Structure
# =====================================================

from .territory import Territory
from .route import Route

from .distributor import Distributor
from .distributor_user import DistributorUser

from .fsr import FSR

# =====================================================
# Customer Management
# =====================================================

from .outlet_category import OutletCategory
from .outlet import Outlet

# =====================================================
# Product Management
# =====================================================

from .product_category import ProductCategory
from .product import Product
from .product_price import ProductPrice

# =====================================================
# Field Operations
# =====================================================

from .visit import Visit
from .visit_note import VisitNote

# =====================================================
# Order Management
# =====================================================

from .order import Order
from .order_item import OrderItem
from .delivery import Delivery

# =====================================================
# System Models
# =====================================================

from .dashboard import Dashboard
from .notification import Notification
from .audit_log import AuditLog


__all__ = [

    # Base
    "BaseModel",

    # Core
    "Company",
    "Subscription",
    "Role",
    "Permission",
    "RolePermission",
    "User",

    # Sales Structure
    "Territory",
    "Route",
    "Distributor",
    "DistributorUser",
    "FSR",

    # Customer Management
    "OutletCategory",
    "Outlet",

    # Product Management
    "ProductCategory",
    "Product",
    "ProductPrice",

    # Field Operations
    "Visit",
    "VisitNote",

    # Order Management
    "Order",
    "OrderItem",
    "Delivery",

    # System
    "Dashboard",
    "Notification",
    "AuditLog",
]