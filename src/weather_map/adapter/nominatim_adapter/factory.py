from geopy.location import Location as GeopyLocation
from weather_map.domain.model.location import Location
from weather_map.domain.model.coordinate import Coordinate


def coordinate_factory_from_geopy_location(
    *, geopy_location: GeopyLocation
) -> Coordinate:
    return Coordinate(
        longitude=geopy_location.longitude,
        latitude=geopy_location.latitude,
    )


def location_factory_from_geopy_location(*, geopy_location: GeopyLocation) -> Location:
    coordinate = coordinate_factory_from_geopy_location(geopy_location=geopy_location)
    return Location(address=geopy_location.address, coordiante=coordinate)
