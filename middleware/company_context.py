"""
Company Context Middleware

Loads the authenticated user's company
into the Flask global request context.
"""

from functools import wraps

from flask import (
    g,
    abort,
)

from .auth import get_current_user


# =====================================================
# Company Context Loader
# =====================================================

def load_company_context():
    """
    Loads the authenticated user's company
    into Flask's global context.

    This function should be registered with:

        app.before_request(load_company_context)
    """

    g.current_user = None
    g.company = None

    user = get_current_user()

    if not user:
        return

    g.current_user = user

    if user.company:

        if (
            user.company.is_active
            and not user.company.is_deleted
        ):

            g.company = user.company


# =====================================================
# Company Required
# =====================================================

def company_required(view):
    """
    Ensures the authenticated user belongs
    to a valid company.
    """

    @wraps(view)
    def wrapped_view(*args, **kwargs):

        if getattr(g, "company", None) is None:

            abort(403)

        return view(*args, **kwargs)

    return wrapped_view


# =====================================================
# Helper Functions
# =====================================================

def get_company():
    """
    Returns the current company.
    """

    return getattr(g, "company", None)


def get_company_id():
    """
    Returns the current company ID.
    """

    company = get_company()

    if company:

        return company.id

    return None


def current_company():
    """
    Alias for get_company().
    """

    return get_company()


def company_exists():
    """
    Returns True if a company has been
    loaded into the request context.
    """

    return get_company() is not None