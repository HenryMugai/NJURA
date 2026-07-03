from functools import wraps

from flask import flash, redirect, request, url_for
from flask_login import current_user


def login_required_custom(view):

    @wraps(view)
    def wrapped_view(*args, **kwargs):

        if not current_user.is_authenticated:
            flash(
                "Please log in first.",
                "warning"
            )

            return redirect(
                url_for(
                    "auth.login",
                    next=request.url
                )
            )

        return view(*args, **kwargs)

    return wrapped_view