from geopy.geocoders import Nominatim as GeopyNominatim
from weather_map.adapter.nominatim_adapter.factory import (
    location_factory_from_geopy_location,
)
from weather_map.domain.model.location import Location
from weather_map.port.geocoding_port import GeocodingDrivenPort


class NominatimAdapter(GeocodingDrivenPort):

    """Adapter class for the Nominatim geocoding service.

    This class implements the GeocodingDrivenPort interface and provides a method to
    perform geocoding searches using the Nominatim service from geopy.

    Attributes
    ----------
        _geolocator (GeopyNominatim): An instance of the Nominatim geolocator.

    """

    def __init__(self: "NominatimAdapter") -> None:
        """Initialize the NominatimAdapter with a Nominatim geolocator instance."""
        self._geolocator = GeopyNominatim(user_agent="py_weather_map")

    def _search(self: "NominatimAdapter", *, search_pattern: str) -> Location:
        """Perform a geocoding search using the Nominatim service.

        Parameters
        ----------
            search_pattern (str): The search pattern or address to geocode.

        Returns
        -------
            Location: A Location instance containing the address and coordinates of the geocoded location.

        """
        geopy_location = self._geolocator.geocode(search_pattern)
        return location_factory_from_geopy_location(geopy_location=geopy_location)
