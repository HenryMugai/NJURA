"""
N.J.U.R.A Service Layer

Contains the application's business logic.

Routes should remain lightweight by delegating
operations to the appropriate service classes.
"""

# =====================================================
# Authentication
# =====================================================

from .auth_service import AuthService

# =====================================================
# Company
# =====================================================

from .company_service import CompanyService

# =====================================================
# Distributor
# =====================================================

from .distributor_service import DistributorService

# =====================================================
# Products
# =====================================================

from .product_service import ProductService

# =====================================================
# Outlets
# =====================================================

from .outlet_service import OutletService

# =====================================================
# Visits
# =====================================================

from .visit_service import VisitService

# =====================================================
# Orders
# =====================================================

from .order_service import OrderService

# =====================================================
# Reports
# =====================================================

from .report_service import ReportService

# =====================================================
# Dashboard
# =====================================================

from .dashboard_service import DashboardService

# =====================================================
# GPS
# =====================================================

from .gps_service import GPSService

# =====================================================
# Notifications
# =====================================================

from .notification_service import NotificationService

# =====================================================
# Analytics
# =====================================================

from .analytics_service import AnalyticsService


__all__ = [

    "AuthService",
    "CompanyService",
    "DistributorService",
    "ProductService",
    "OutletService",
    "VisitService",
    "OrderService",
    "ReportService",
    "DashboardService",
    "GPSService",
    "NotificationService",
    "AnalyticsService",
]