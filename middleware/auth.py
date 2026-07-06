"""
Authentication Middleware

Provides decorators used to protect routes
that require authenticated users.
"""

from functools import wraps

from flask import (
    flash,
    g,
    redirect,
    request,
    session,
    url_for,
)

from models import User


# =====================================================
# Current User Loader
# =====================================================

def get_current_user():
    """
    Returns the currently authenticated user.

    Returns:
        User | None
    """

    user_id = session.get("user_id")

    if not user_id:
        return None

    return User.query.filter_by(
        id=user_id,
        is_active=True,
        is_deleted=False
    ).first()


# =====================================================
# Login Required
# =====================================================

def login_required(view):
    """
    Protects routes that require authentication.
    """

    @wraps(view)
    def wrapped_view(*args, **kwargs):

        user = get_current_user()

        if not user:

            flash(
                "Please login to continue.",
                "warning"
            )

            return redirect(
                url_for(
                    "auth.login",
                    next=request.url
                )
            )

        g.current_user = user

        return view(*args, **kwargs)

    return wrapped_view


# =====================================================
# Guest Required
# =====================================================

def guest_required(view):
    """
    Prevents authenticated users from
    accessing guest-only pages.
    """

    @wraps(view)
    def wrapped_view(*args, **kwargs):

        user = get_current_user()

        if user:

            return redirect(
                url_for("public.index")
            )

        return view(*args, **kwargs)

    return wrapped_view


# =====================================================
# Session Helpers
# =====================================================

def login_user(user):
    """
    Creates a login session.
    """

    session.clear()

    session["user_id"] = user.id

    session.permanent = True


def logout_user():
    """
    Destroys the current session.
    """

    session.clear()


# =====================================================
# Authentication Helpers
# =====================================================

def is_authenticated():
    """
    Returns True if a user is logged in.
    """

    return session.get("user_id") is not None


def current_user():
    """
    Shortcut for retrieving the
    currently logged in user.
    """

    return get_current_user()