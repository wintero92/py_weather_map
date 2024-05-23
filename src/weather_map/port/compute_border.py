from abc import abstractmethod

from weather_map.domain.model.border import Border
from weather_map.domain.model.location import Location


class ComputeBorder:
    def compute_border(self, *, location: Location) -> Border:
        return self._compute_border(location=location)

    @abstractmethod
    def _compute_border(self, *, location: Location) -> Border:
        raise NotImplementedError
