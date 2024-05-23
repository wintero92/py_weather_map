from abc import abstractmethod

from weather_map.domain.model.location import Location


class GeocodingDrivenPort:
    """GeocodingDrivenPort is an interface for geocoding services.

    Methods
    -------
        search(search_pattern: str) -> Location:
            Public method that delegates the search operation to the _search method.

    Abstract Methods:
        _search(search_pattern: str) -> Location:
            Abstract method to be implemented by subclasses for performing the geocoding search operation.

    """

    def search(self: "GeocodingDrivenPort", *, search_pattern: str) -> Location:
        """Public method to search for a location using the given search pattern.

        Args:
        ----
            search_pattern (str): The pattern to search for the location.

        Returns:
        -------
            Location: The location object resulting from the search.

        Delegates the actual search operation to the _search method.

        """
        return self._search(search_pattern=search_pattern)

    @abstractmethod
    def _search(self: "GeocodingDrivenPort", *, search_pattern: str) -> Location:
        raise NotImplementedError
