"""
Permission Utilities

Helper functions for role and
permission management.
"""

from models import (
    Permission,
    Role,
    RolePermission,
    User,
)


# =====================================================
# User
# =====================================================

def get_user(user_id):
    """
    Returns a user.
    """

    return User.query.filter_by(
        id=user_id,
        is_deleted=False
    ).first()


# =====================================================
# Role
# =====================================================

def get_role(role_id):
    """
    Returns a role.
    """

    return Role.query.filter_by(
        id=role_id
    ).first()


# =====================================================
# Permission
# =====================================================

def get_permission(permission_name):
    """
    Returns a permission.
    """

    return Permission.query.filter_by(
        name=permission_name
    ).first()


# =====================================================
# User Role
# =====================================================

def user_role(user):
    """
    Returns a user's role.
    """

    if not user:

        return None

    return user.role


# =====================================================
# Permission Check
# =====================================================

def has_permission(
    user,
    permission_name
):
    """
    Checks whether a user has
    a specific permission.
    """

    if not user:

        return False

    permission = Permission.query.filter_by(
        name=permission_name,
        permission_status="Active"
    ).first()

    if not permission:

        return False

    role_permission = RolePermission.query.filter_by(

        role_id=user.role_id,

        permission_id=permission.id,

        is_allowed=True,

        is_deleted=False

    ).first()

    return role_permission is not None


# =====================================================
# Multiple Permissions
# =====================================================

def has_any_permission(
    user,
    permissions
):
    """
    Returns True if the user has
    at least one permission.
    """

    return any(

        has_permission(
            user,
            permission
        )

        for permission in permissions

    )


def has_all_permissions(
    user,
    permissions
):
    """
    Returns True if the user has
    every permission.
    """

    return all(

        has_permission(
            user,
            permission
        )

        for permission in permissions

    )


# =====================================================
# Role Checks
# =====================================================

def has_role(
    user,
    role_name
):
    """
    Checks whether the user
    has a specific role.
    """

    if not user:

        return False

    if not user.role:

        return False

    return user.role.name == role_name


def has_any_role(
    user,
    roles
):
    """
    Checks multiple roles.
    """

    return any(

        has_role(
            user,
            role
        )

        for role in roles

    )


# =====================================================
# Permission List
# =====================================================

def user_permissions(user):
    """
    Returns a list of permission
    names assigned to the user.
    """

    if not user:

        return []

    permissions = (

        Permission.query

        .join(

            RolePermission,

            Permission.id == RolePermission.permission_id

        )

        .filter(

            RolePermission.role_id == user.role_id,

            RolePermission.is_allowed == True,

            Permission.permission_status == "Active",

            Permission.is_deleted == False,

            RolePermission.is_deleted == False

        )

        .all()

    )

    return [

        permission.name

        for permission in permissions

    ]