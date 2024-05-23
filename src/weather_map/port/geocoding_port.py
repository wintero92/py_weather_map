from abc import abstractmethod

from weather_map.domain.model.location import Location


class GeocodingDrivenPort:
    def search(self, *, search_pattern: str) -> Location:
        return self._search(search_pattern=search_pattern)

    @abstractmethod
    def _search(self, *, search_pattern: str) -> Location:
        raise NotImplementedError
