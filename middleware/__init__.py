"""
N.J.U.R.A Middleware Package

This package contains middleware decorators and
request handlers responsible for:

    • Authentication
    • Role-based access control
    • Permission checks
    • Company (Tenant) context
    • Subscription validation
"""

# =====================================================
# Authentication
# =====================================================

from .auth import (
    login_required,
    guest_required,
)

# =====================================================
# Roles
# =====================================================

from .roles import (
    role_required,
)

# =====================================================
# Permissions
# =====================================================

from .permissions import (
    permission_required,
)

# =====================================================
# Company Context
# =====================================================

from .company_context import (
    load_company_context,
)

# =====================================================
# Subscription
# =====================================================

from .subscription import (
    subscription_required,
)

# =====================================================
# Public Exports
# =====================================================

__all__ = [

    # Authentication
    "login_required",
    "guest_required",

    # Roles
    "role_required",

    # Permissions
    "permission_required",

    # Company Context
    "load_company_context",

    # Subscription
    "subscription_required",
]