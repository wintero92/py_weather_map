from geopy.location import Location as GeopyLocation
from weather_map.domain.model.coordinate import Coordinate
from weather_map.domain.model.location import Location


def coordinate_factory_from_geopy_location(
    *,
    geopy_location: GeopyLocation,
) -> Coordinate:
    """Create a Coordinate instance from a GeopyLocation object.

    Args:
    ----
    - geopy_location (GeopyLocation): The GeopyLocation object from which to extract coordinates.

    Returns:
    -------
    - Coordinate: A Coordinate instance with latitude and longitude from the GeopyLocation.

    """
    return Coordinate(
        longitude=geopy_location.longitude,
        latitude=geopy_location.latitude,
    )


def location_factory_from_geopy_location(*, geopy_location: GeopyLocation) -> Location:
    """Create a Location instance from a GeopyLocation object.

    Args:
    ----
    - geopy_location (GeopyLocation): The GeopyLocation object from which to extract the address and coordinates.

    Returns:
    -------
    - Location: A Location instance with address and coordinates from the GeopyLocation.

    """
    coordinate = coordinate_factory_from_geopy_location(geopy_location=geopy_location)
    return Location(address=geopy_location.address, coordinate=coordinate)
