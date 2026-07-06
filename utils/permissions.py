"""
Application Validators

Validation helpers used throughout
the N.J.U.R.A platform.
"""

import re

from models import (
    Company,
    Distributor,
    Outlet,
    Product,
    Role,
    User,
)


# =====================================================
# Email
# =====================================================

def is_valid_email(email):
    """
    Validates an email address.
    """

    if not email:

        return False

    pattern = (
        r"^[A-Za-z0-9._%+-]+"
        r"@[A-Za-z0-9.-]+"
        r"\.[A-Za-z]{2,}$"
    )

    return bool(
        re.match(pattern, email)
    )


# =====================================================
# Phone Number
# =====================================================

def is_valid_phone(phone):
    """
    Validates a phone number.
    """

    if not phone:

        return False

    pattern = r"^\+?[0-9]{9,15}$"

    return bool(
        re.match(pattern, phone)
    )


# =====================================================
# Password
# =====================================================

def is_valid_password(password):
    """
    Basic password validation.
    """

    if not password:

        return False

    return len(password) >= 8


# =====================================================
# Username
# =====================================================

def is_valid_username(username):
    """
    Validates a username.
    """

    if not username:

        return False

    pattern = r"^[A-Za-z0-9_.-]{3,50}$"

    return bool(
        re.match(pattern, username)
    )


# =====================================================
# Company
# =====================================================

def company_exists(company_id):
    """
    Checks whether a company exists.
    """

    return Company.query.filter_by(
        id=company_id,
        is_deleted=False
    ).first() is not None


# =====================================================
# User
# =====================================================

def username_exists(
    company_id,
    username
):
    """
    Checks whether a username exists.
    """

    return User.query.filter_by(

        company_id=company_id,

        username=username,

        is_deleted=False

    ).first() is not None


def email_exists(email):
    """
    Checks whether an email exists.
    """

    return User.query.filter_by(

        email=email,

        is_deleted=False

    ).first() is not None


# =====================================================
# Role
# =====================================================

def role_exists(role_id):
    """
    Checks whether a role exists.
    """

    return Role.query.filter_by(
        id=role_id
    ).first() is not None


# =====================================================
# Product
# =====================================================

def product_exists(
    company_id,
    product_id
):
    """
    Checks whether a product exists.
    """

    return Product.query.filter_by(

        id=product_id,

        company_id=company_id,

        is_deleted=False

    ).first() is not None


# =====================================================
# Outlet
# =====================================================

def outlet_exists(
    company_id,
    outlet_id
):
    """
    Checks whether an outlet exists.
    """

    return Outlet.query.filter_by(

        id=outlet_id,

        company_id=company_id,

        is_deleted=False

    ).first() is not None


# =====================================================
# Distributor
# =====================================================

def distributor_exists(
    company_id,
    distributor_id
):
    """
    Checks whether a distributor exists.
    """

    return Distributor.query.filter_by(

        id=distributor_id,

        company_id=company_id,

        is_deleted=False

    ).first() is not None


# =====================================================
# Numeric
# =====================================================

def is_positive_number(value):
    """
    Checks whether a value
    is a positive number.
    """

    try:

        return float(value) >= 0

    except (ValueError, TypeError):

        return False


# =====================================================
# Required Fields
# =====================================================

def validate_required(
    data,
    fields
):
    """
    Validates required fields.

    Returns:
        (True, None)
        (False, "field_name")
    """

    for field in fields:

        value = data.get(field)

        if value in [

            None,

            "",

            []

        ]:

            return False, field

    return True, None


# =====================================================
# GPS
# =====================================================

def is_valid_latitude(latitude):
    """
    Validates latitude.
    """

    try:

        latitude = float(latitude)

        return -90 <= latitude <= 90

    except (TypeError, ValueError):

        return False


def is_valid_longitude(longitude):
    """
    Validates longitude.
    """

    try:

        longitude = float(longitude)

        return -180 <= longitude <= 180

    except (TypeError, ValueError):

        return False


# =====================================================
# Coordinates
# =====================================================

def valid_coordinates(
    latitude,
    longitude
):
    """
    Validates GPS coordinates.
    """

    return (

        is_valid_latitude(latitude)

        and

        is_valid_longitude(longitude)

    )