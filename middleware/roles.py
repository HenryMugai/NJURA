"""
Role Middleware

Provides decorators for restricting
access based on user roles.
"""

from functools import wraps

from flask import (
    flash,
    g,
    redirect,
    url_for,
)

from .auth import get_current_user


# =====================================================
# Role Required
# =====================================================

def role_required(*allowed_roles):
    """
    Restricts access to one or more roles.

    Example:

        @login_required
        @role_required("Super Admin")

    or

        @login_required
        @role_required(
            "Company Admin",
            "Distributor"
        )
    """

    def decorator(view):

        @wraps(view)
        def wrapped_view(*args, **kwargs):

            user = get_current_user()

            if not user:

                flash(
                    "Please login to continue.",
                    "warning"
                )

                return redirect(
                    url_for("auth.login")
                )

            if not user.role:

                flash(
                    "No role has been assigned to your account.",
                    "danger"
                )

                return redirect(
                    url_for("auth.login")
                )

            if user.role.name not in allowed_roles:

                flash(
                    "You do not have permission to access this page.",
                    "danger"
                )

                return redirect(
                    url_for("public.index")
                )

            g.current_user = user

            return view(*args, **kwargs)

        return wrapped_view

    return decorator


# =====================================================
# Helper Functions
# =====================================================

def has_role(user, *roles):
    """
    Returns True if the user belongs
    to one of the supplied roles.
    """

    if not user:
        return False

    if not user.role:
        return False

    return user.role.name in roles


def is_super_admin(user):
    """
    Returns True if user is
    the platform Super Admin.
    """

    return has_role(
        user,
        "Super Admin"
    )


def is_company_admin(user):
    """
    Returns True if user is
    a Company Administrator.
    """

    return has_role(
        user,
        "Company Admin"
    )


def is_distributor(user):
    """
    Returns True if user belongs
    to a distributor.
    """

    return has_role(
        user,
        "Distributor"
    )


def is_fsr(user):
    """
    Returns True if user is an FSR.
    """

    return has_role(
        user,
        "FSR"
    )