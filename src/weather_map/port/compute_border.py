from abc import abstractmethod

from weather_map.domain.model.nominatim import Nominatim
from weather_map.domain.model.border import Border


class ComputeBorder:
    def compute_border(self, *, nominatim: Nominatim) -> Border:
        return self._compute_border(nominatim=nominatim)

    @abstractmethod
    def _compute_border(self, *, nominatim: Nominatim) -> Border:
        raise NotImplementedError
