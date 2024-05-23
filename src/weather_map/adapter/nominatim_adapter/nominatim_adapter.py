from geopy.geocoders import Nominatim as GeopyNominatim
from geopy.location import Location as GeopyLocation
from weather_map.adapter.nominatim_adapter.factory import (
    location_factory_from_geopy_location,
)
from weather_map.domain.model.location import Location
from weather_map.port.geocoding_port import GeocodingDrivenPort


class NominatimAdapter(GeocodingDrivenPort):

    def __init__(self) -> None:
        self._geolocator = GeopyNominatim(user_agent="py_weather_map")

    def _search(self, *, search_pattern: str) -> Location:
        geopy_location: GeopyLocation = self._geolocator.geocode(search_pattern)
        return location_factory_from_geopy_location(geopy_location=geopy_location)
