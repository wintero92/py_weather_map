from abc import abstractmethod

from weather_map.domain.model.border import Border
from weather_map.domain.model.location import Location


class ComputeBorder:
    """ComputeBorder is an interface for computing the border of a given location.

    Methods
    -------
    compute_border(location: Location) -> Border:
        Public method that delegates the border computation to the _compute_border method.

    Abstract Methods:
    _compute_border(location: Location) -> Border:
        Abstract method to be implemented by subclasses for performing the border computation.

    """

    def compute_border(self: "ComputeBorder", *, location: Location) -> Border:
        """Compute the border for a given Location instance.

        Args:
        ----
            location (Location): The Location instance to compute the border from.

        Returns:
        -------
            Border: A Border instance computed from the Location data.

        """
        return self._compute_border(location=location)

    @abstractmethod
    def _compute_border(self: "ComputeBorder", *, location: Location) -> Border:
        raise NotImplementedError
