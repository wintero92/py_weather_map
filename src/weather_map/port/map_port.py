from abc import abstractmethod

from weather_map.domain.model.border import Border


class MapPort:

    """An abstract base class that defines the interface for adding borders to a map.

    Methods
    -------
    add_border(border: Border) -> None
        Adds a border to the map by calling the abstract _add_border method.

    _add_border(border: Border) -> None
        Abstract method to be implemented by subclasses to add a border to the map.

    show_in_browser() -> None
        Displays the map in a browser by calling the abstract _show_in_browser method.

    _show_in_browser() -> None
        Abstract method to be implemented by subclasses to display the map in a browser.

    """

    def add_border(self: "MapPort", *, border: Border) -> None:
        """Add a border to the map.

        Parameters
        ----------
        border : Border
            The border object to be added to the map.

        Returns
        -------
        None

        """
        return self._add_border(border=border)

    @abstractmethod
    def _add_border(self: "MapPort", *, border: Border) -> None:
        raise NotImplementedError

    def show_in_browser(self: "MapPort") -> None:
        """Display the map in a browser.

        Returns
        -------
        None

        """
        return self._show_in_browser()

    @abstractmethod
    def _show_in_browser(self: "MapPort") -> None:
        raise NotImplementedError
