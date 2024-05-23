from abc import ABC, abstractmethod

from weather_map.domain.model.location import Location


class GeocodingDrivenPort(ABC):

    """Driven port abstracting geocoding operations.

    A base class for geocoding service ports that defines a standard interface for
    geocoding operations.

    This class provides a template method `search` that calls the `_search` method, which must be implemented
    by subclasses to provide the actual geocoding functionality.

    Methods
    -------
    - search: Template method that calls the `_search` method to perform a geocoding search.
    - _search: Abstract method that subclasses must implement to provide geocoding search functionality.

    """

    def search(self: "GeocodingDrivenPort", *, search_pattern: str) -> Location:
        """Perform a geocoding search using the provided search pattern.

        This is a template method that calls the `_search` method, which must be implemented by subclasses.

        Parameters
        ----------
        - search_pattern: A string containing the search pattern or address to geocode.

        Returns
        -------
        - Location: The geocoded location corresponding to the search pattern.

        """
        return self._search(search_pattern=search_pattern)

    @abstractmethod
    def _search(self: "GeocodingDrivenPort", *, search_pattern: str) -> Location:
        raise NotImplementedError
