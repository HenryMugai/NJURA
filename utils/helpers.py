"""
Application Helper Functions

Common utility functions used throughout
the N.J.U.R.A platform.
"""

import random
import string
import uuid
from datetime import datetime

from slugify import slugify


# =====================================================
# UUID
# =====================================================

def generate_uuid():
    """
    Generates a UUID string.
    """

    return str(uuid.uuid4())


# =====================================================
# Slug
# =====================================================

def generate_slug(text):
    """
    Generates a URL-friendly slug.
    """

    return slugify(text)


# =====================================================
# Reference Numbers
# =====================================================

def generate_reference(
    prefix,
    length=6
):
    """
    Generates a reference number.

    Example:
        ORD-4X92JK
    """

    random_string = "".join(

        random.choices(

            string.ascii_uppercase
            + string.digits,

            k=length

        )

    )

    return f"{prefix}-{random_string}"


# =====================================================
# Random Code
# =====================================================

def generate_code(
    length=8
):
    """
    Generates a random code.
    """

    return "".join(

        random.choices(

            string.ascii_uppercase
            + string.digits,

            k=length

        )

    )


# =====================================================
# Timestamp
# =====================================================

def current_timestamp():
    """
    Returns current UTC datetime.
    """

    return datetime.utcnow()


# =====================================================
# Date Formatting
# =====================================================

def format_date(
    value,
    fmt="%d/%m/%Y"
):
    """
    Formats a date.
    """

    if not value:

        return ""

    return value.strftime(fmt)


def format_datetime(
    value,
    fmt="%d/%m/%Y %H:%M"
):
    """
    Formats a datetime.
    """

    if not value:

        return ""

    return value.strftime(fmt)


# =====================================================
# Currency
# =====================================================

def format_currency(
    amount,
    currency="KES"
):
    """
    Formats a currency amount.
    """

    if amount is None:

        amount = 0

    return f"{currency} {float(amount):,.2f}"


# =====================================================
# Percentage
# =====================================================

def percentage(
    numerator,
    denominator
):
    """
    Calculates percentage.
    """

    if denominator == 0:

        return 0

    return round(

        (numerator / denominator) * 100,

        2

    )


# =====================================================
# Full Name
# =====================================================

def full_name(
    first_name,
    middle_name=None,
    last_name=None
):
    """
    Builds a full name.
    """

    return " ".join(

        filter(

            None,

            [

                first_name,

                middle_name,

                last_name

            ]

        )

    )


# =====================================================
# Boolean Conversion
# =====================================================

def to_bool(value):
    """
    Converts a value to boolean.
    """

    if isinstance(value, bool):

        return value

    return str(value).lower() in [

        "true",

        "1",

        "yes",

        "on"

    ]


# =====================================================
# Safe Integer
# =====================================================

def to_int(
    value,
    default=0
):
    """
    Safely converts to integer.
    """

    try:

        return int(value)

    except (TypeError, ValueError):

        return default


# =====================================================
# Safe Float
# =====================================================

def to_float(
    value,
    default=0.0
):
    """
    Safely converts to float.
    """

    try:

        return float(value)

    except (TypeError, ValueError):

        return default


# =====================================================
# Empty Check
# =====================================================

def is_empty(value):
    """
    Checks if value is empty.
    """

    return value in [

        None,

        "",

        [],

        {},

        ()

    ]


# =====================================================
# Text Cleaning
# =====================================================

def clean_text(text):
    """
    Cleans whitespace.
    """

    if not text:

        return ""

    return " ".join(

        str(text).split()

    )