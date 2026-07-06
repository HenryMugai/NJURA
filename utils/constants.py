"""
Application Constants

System-wide constants used throughout
the N.J.U.R.A platform.
"""

# =====================================================
# Company
# =====================================================

DEFAULT_COUNTRY = "Kenya"

DEFAULT_CURRENCY = "KES"

DEFAULT_TIMEZONE = "Africa/Nairobi"

DEFAULT_DATE_FORMAT = "DD/MM/YYYY"

# =====================================================
# Authentication
# =====================================================

MAX_LOGIN_ATTEMPTS = 5

ACCOUNT_LOCK_MINUTES = 30

PASSWORD_MIN_LENGTH = 8

# =====================================================
# Pagination
# =====================================================

DEFAULT_PAGE = 1

DEFAULT_PER_PAGE = 20

MAX_PER_PAGE = 100

# =====================================================
# GPS
# =====================================================

DEFAULT_GEOFENCE_RADIUS = 100  # metres

EARTH_RADIUS_KM = 6371

# =====================================================
# Subscription
# =====================================================

TRIAL_PERIOD_DAYS = 30

DEFAULT_MAX_USERS = 20

DEFAULT_MAX_FSRS = 10

DEFAULT_MAX_PRODUCTS = 500

DEFAULT_MAX_OUTLETS = 1000

DEFAULT_MAX_DISTRIBUTORS = 20

# =====================================================
# User Status
# =====================================================

USER_PENDING = "Pending"

USER_ACTIVE = "Active"

USER_SUSPENDED = "Suspended"

USER_LOCKED = "Locked"

USER_ARCHIVED = "Archived"

# =====================================================
# Company Status
# =====================================================

COMPANY_PENDING = "Pending"

COMPANY_ACTIVE = "Active"

COMPANY_SUSPENDED = "Suspended"

COMPANY_ARCHIVED = "Archived"

# =====================================================
# Subscription Status
# =====================================================

SUBSCRIPTION_TRIAL = "Trial"

SUBSCRIPTION_ACTIVE = "Active"

SUBSCRIPTION_EXPIRED = "Expired"

SUBSCRIPTION_GRACE = "Grace Period"

SUBSCRIPTION_SUSPENDED = "Suspended"

SUBSCRIPTION_CANCELLED = "Cancelled"

# =====================================================
# Order Status
# =====================================================

ORDER_DRAFT = "Draft"

ORDER_SUBMITTED = "Submitted"

ORDER_PROCESSING = "Processing"

ORDER_READY = "Ready for Dispatch"

ORDER_DISPATCHED = "Dispatched"

ORDER_DELIVERED = "Delivered"

ORDER_CANCELLED = "Cancelled"

# =====================================================
# Approval Status
# =====================================================

APPROVAL_PENDING = "Pending"

APPROVAL_APPROVED = "Approved"

APPROVAL_REJECTED = "Rejected"

# =====================================================
# Payment Status
# =====================================================

PAYMENT_PENDING = "Pending"

PAYMENT_PARTIAL = "Partially Paid"

PAYMENT_PAID = "Paid"

# =====================================================
# Delivery Status
# =====================================================

DELIVERY_PENDING = "Pending"

DELIVERY_PREPARING = "Preparing"

DELIVERY_DISPATCHED = "Dispatched"

DELIVERY_IN_TRANSIT = "In Transit"

DELIVERY_DELIVERED = "Delivered"

DELIVERY_PARTIAL = "Partially Delivered"

DELIVERY_FAILED = "Failed"

DELIVERY_RETURNED = "Returned"

DELIVERY_CANCELLED = "Cancelled"

# =====================================================
# Visit Status
# =====================================================

VISIT_OPEN = "Open"

VISIT_COMPLETED = "Completed"

VISIT_CANCELLED = "Cancelled"

# =====================================================
# Notification Status
# =====================================================

NOTIFICATION_PENDING = "Pending"

NOTIFICATION_SENT = "Sent"

NOTIFICATION_DELIVERED = "Delivered"

NOTIFICATION_READ = "Read"

NOTIFICATION_FAILED = "Failed"

# =====================================================
# Dashboard
# =====================================================

AUTO_REFRESH_SECONDS = 300

DEFAULT_DASHBOARD_NAME = "Default Dashboard"

# =====================================================
# API
# =====================================================

SUCCESS = "success"

ERROR = "error"

WARNING = "warning"

INFO = "info"