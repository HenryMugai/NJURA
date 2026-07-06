"""
GPS Service

Handles GPS validation, distance calculations
and location-based business logic.
"""

from math import (
    asin,
    cos,
    radians,
    sin,
    sqrt,
)


class GPSService:
    """
    GPS utility service.
    """

    EARTH_RADIUS_KM = 6371.0

    # =====================================================
    # Distance Calculation
    # =====================================================

    @staticmethod
    def calculate_distance(
        latitude_one,
        longitude_one,
        latitude_two,
        longitude_two
    ):
        """
        Calculates the distance between two
        GPS coordinates using the Haversine formula.

        Returns:
            Distance in kilometres.
        """

        latitude_one = radians(float(latitude_one))
        longitude_one = radians(float(longitude_one))

        latitude_two = radians(float(latitude_two))
        longitude_two = radians(float(longitude_two))

        delta_latitude = (
            latitude_two - latitude_one
        )

        delta_longitude = (
            longitude_two - longitude_one
        )

        a = (

            sin(delta_latitude / 2) ** 2

            +

            cos(latitude_one)
            * cos(latitude_two)

            * sin(delta_longitude / 2) ** 2

        )

        c = 2 * asin(sqrt(a))

        return GPSService.EARTH_RADIUS_KM * c

    # =====================================================
    # Metres Conversion
    # =====================================================

    @staticmethod
    def distance_in_metres(
        latitude_one,
        longitude_one,
        latitude_two,
        longitude_two
    ):
        """
        Returns distance in metres.
        """

        return round(

            GPSService.calculate_distance(

                latitude_one,

                longitude_one,

                latitude_two,

                longitude_two

            ) * 1000,

            2

        )

    # =====================================================
    # Geofence Validation
    # =====================================================

    @staticmethod
    def within_radius(
        outlet_latitude,
        outlet_longitude,
        current_latitude,
        current_longitude,
        radius_metres=100
    ):
        """
        Determines whether the current
        location is within the allowed
        radius from the outlet.
        """

        distance = GPSService.distance_in_metres(

            outlet_latitude,

            outlet_longitude,

            current_latitude,

            current_longitude

        )

        return distance <= radius_metres

    # =====================================================
    # Coordinate Validation
    # =====================================================

    @staticmethod
    def valid_coordinates(
        latitude,
        longitude
    ):
        """
        Validates GPS coordinates.
        """

        try:

            latitude = float(latitude)
            longitude = float(longitude)

        except Exception:

            return False

        return (

            -90 <= latitude <= 90

            and

            -180 <= longitude <= 180

        )

    # =====================================================
    # Coordinate Formatting
    # =====================================================

    @staticmethod
    def format_coordinates(
        latitude,
        longitude
    ):
        """
        Returns formatted GPS coordinates.
        """

        return (

            round(float(latitude), 6),

            round(float(longitude), 6)

        )

    # =====================================================
    # Visit Validation
    # =====================================================

    @staticmethod
    def validate_visit_location(
        outlet,
        latitude,
        longitude,
        radius=100
    ):
        """
        Validates whether an FSR is
        within the permitted visit radius.
        """

        if not outlet.latitude:

            return False

        if not outlet.longitude:

            return False

        return GPSService.within_radius(

            outlet.latitude,

            outlet.longitude,

            latitude,

            longitude,

            radius

        )

    # =====================================================
    # Google Maps URL
    # =====================================================

    @staticmethod
    def maps_url(
        latitude,
        longitude
    ):
        """
        Generates a Google Maps URL.
        """

        return (

            "https://maps.google.com/?q="

            f"{latitude},{longitude}"

        )

    # =====================================================
    # Navigation URL
    # =====================================================

    @staticmethod
    def navigation_url(
        latitude,
        longitude
    ):
        """
        Generates a Google Maps
        navigation URL.
        """

        return (

            "https://www.google.com/maps/dir/?api=1"

            f"&destination={latitude},{longitude}"

        )