"""
Subscription Middleware

Ensures a company's subscription is valid
before allowing access to protected routes.
"""

from datetime import date
from functools import wraps

from flask import (
    flash,
    g,
    redirect,
    url_for,
)

from .auth import get_current_user


# =====================================================
# Subscription Required
# =====================================================

def subscription_required(view):
    """
    Ensures the authenticated user's company
    has an active subscription.
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
                url_for("auth.login")
            )

        company = user.company

        # Super Admin does not require
        # a company subscription.
        if company is None:

            g.current_user = user

            return view(*args, **kwargs)

        subscription = company.subscriptions.filter_by(
            status="Active"
        ).order_by(
            company.subscriptions.property.mapper.class_.created_at.desc()
        ).first()

        if subscription is None:

            flash(
                "Your company does not have an active subscription.",
                "danger"
            )

            return redirect(
                url_for("public.subscription_required")
            )

        today = date.today()

        if subscription.end_date < today:

            flash(
                "Your company subscription has expired.",
                "warning"
            )

            return redirect(
                url_for("public.subscription_required")
            )

        if not company.is_active:

            flash(
                "Your company account has been suspended.",
                "danger"
            )

            return redirect(
                url_for("public.subscription_required")
            )

        g.current_user = user
        g.company = company
        g.subscription = subscription

        return view(*args, **kwargs)

    return wrapped_view


# =====================================================
# Helper Functions
# =====================================================

def get_subscription():
    """
    Returns the current company subscription.
    """

    return getattr(
        g,
        "subscription",
        None
    )


def subscription_active():
    """
    Returns True if an active subscription
    exists in the current request.
    """

    return get_subscription() is not None


def subscription_expired():
    """
    Returns True if the current subscription
    has expired.
    """

    subscription = get_subscription()

    if subscription is None:
        return True

    return subscription.end_date < date.today()


def subscription_days_remaining():
    """
    Returns the remaining subscription days.
    """

    subscription = get_subscription()

    if subscription is None:
        return 0

    remaining = (
        subscription.end_date - date.today()
    ).days

    return max(remaining, 0)