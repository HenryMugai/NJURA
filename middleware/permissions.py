"""
Permission Middleware

Provides decorators for restricting access
based on user permissions.
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
# Permission Required
# =====================================================

def permission_required(*required_permissions):
    """
    Restricts access to users having one or more
    required permissions.

    Example:

        @permission_required("users.view")

        @permission_required(
            "orders.create",
            "orders.edit"
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
                    "Your account has not been assigned a role.",
                    "danger"
                )

                return redirect(
                    url_for("public.index")
                )

            user_permissions = {

                rp.permission.name

                for rp in user.role.role_permissions

                if (
                    rp.is_allowed
                    and rp.permission
                    and rp.permission.permission_status == "Active"
                )

            }

            if not any(
                permission in user_permissions
                for permission in required_permissions
            ):

                flash(
                    "You do not have permission to perform this action.",
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

def has_permission(user, permission_name):
    """
    Returns True if the user has the
    specified permission.
    """

    if not user:
        return False

    if not user.role:
        return False

    permissions = {

        rp.permission.name

        for rp in user.role.role_permissions

        if (
            rp.is_allowed
            and rp.permission
            and rp.permission.permission_status == "Active"
        )

    }

    return permission_name in permissions


def has_any_permission(user, *permissions):
    """
    Returns True if the user has at least
    one of the supplied permissions.
    """

    return any(
        has_permission(user, permission)
        for permission in permissions
    )


def has_all_permissions(user, *permissions):
    """
    Returns True if the user has all
    supplied permissions.
    """

    return all(
        has_permission(user, permission)
        for permission in permissions
    )