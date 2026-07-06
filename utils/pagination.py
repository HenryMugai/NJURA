"""
Pagination Utilities

Provides helper functions for paginating
SQLAlchemy query results.
"""

from math import ceil


# =====================================================
# Pagination
# =====================================================

def paginate(
    query,
    page=1,
    per_page=20
):
    """
    Paginates a SQLAlchemy query.

    Returns:
        Dictionary containing
        pagination metadata and items.
    """

    page = max(int(page), 1)

    per_page = max(int(per_page), 1)

    total = query.count()

    total_pages = ceil(
        total / per_page
    ) if total else 1

    items = query.offset(

        (page - 1) * per_page

    ).limit(

        per_page

    ).all()

    return {

        "items": items,

        "page": page,

        "per_page": per_page,

        "total": total,

        "total_pages": total_pages,

        "has_next": page < total_pages,

        "has_previous": page > 1,

        "next_page": (
            page + 1
            if page < total_pages
            else None
        ),

        "previous_page": (
            page - 1
            if page > 1
            else None
        )

    }


# =====================================================
# Metadata Only
# =====================================================

def pagination_metadata(
    total,
    page,
    per_page
):
    """
    Returns pagination metadata.
    """

    total_pages = ceil(
        total / per_page
    ) if total else 1

    return {

        "page": page,

        "per_page": per_page,

        "total": total,

        "total_pages": total_pages,

        "has_next": page < total_pages,

        "has_previous": page > 1,

        "next_page": (
            page + 1
            if page < total_pages
            else None
        ),

        "previous_page": (
            page - 1
            if page > 1
            else None
        )

    }


# =====================================================
# Offset
# =====================================================

def calculate_offset(
    page,
    per_page
):
    """
    Calculates SQL offset.
    """

    page = max(
        int(page),
        1
    )

    return (

        page - 1

    ) * int(per_page)


# =====================================================
# Limit
# =====================================================

def calculate_limit(
    per_page
):
    """
    Returns SQL limit.
    """

    return max(
        int(per_page),
        1
    )