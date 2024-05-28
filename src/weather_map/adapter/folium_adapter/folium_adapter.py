import folium
from weather_map.adapter.folium_adapter.factory import border_to_geojson
from weather_map.domain.model.border import Border
from weather_map.domain.model.coordinate import Coordinate
from weather_map.port.map_port import MapPort

# SLF001 Private member accessed


class FoliumAdapter(MapPort):

    """Adapter class for Folium that extends the MapPort abstract base class.

    This class provides methods to add borders to a map and display the map in a browser using the Folium library.

    Attributes
    ----------
    _map : folium.Map
        The Folium Map object used to render the map.

    Methods
    -------
    __init__() -> None
        Initializes the Folium Map with OpenStreetMap tiles.
    _update_map_init_state(zoom_start: int, center_of_map: Coordinate) -> None
        Updates the map's initial state with the given zoom level and center coordinates.
    _add_border(border: Border) -> None
        Adds a border to the map using GeoJSON and updates the map's initial state.
    _show_in_browser() -> None
        Displays the map in a browser.

    """

    def __init__(self: "FoliumAdapter") -> None:
        """Initialize the Folium Map with OpenStreetMap tiles."""
        self._map = folium.Map(
            tiles="OpenStreetMap",
        )

    def _update_map_init_state(
        self: "FoliumAdapter",
        *,
        zoom_start: int,
        center_of_map: Coordinate,
    ) -> None:
        """Update the map's initial state with the given zoom level and center coordinates.

        Parameters
        ----------
        zoom_start : int
            The initial zoom level of the map.
        center_of_map : Coordinate
            The coordinates of the center of the map.

        Returns
        -------
        None

        """
        new_map = folium.Map(
            location=(center_of_map.latitude, center_of_map.longitude),
            zoom_start=zoom_start,
            tiles="OpenStreetMap",
        )
        for child in list(self._map._children.values()):  # noqa: SLF001
            new_map.add_child(child)
        self._map = new_map

    def _add_border(self: "FoliumAdapter", *, border: Border) -> None:
        """Add a border to the map using GeoJSON and updates the map's initial state.

        Parameters
        ----------
        border : Border
            The border object to be added to the map.

        Returns
        -------
        None

        """
        border_geojson = border_to_geojson(border=border)
        folium.GeoJson(
            border_geojson,
            style_function=lambda _: {"color": "blue", "weight": 2, "fillOpacity": 0.1},
        ).add_to(parent=self._map)
        self._update_map_init_state(zoom_start=5, center_of_map=border.centroid)

    def _show_in_browser(self: "FoliumAdapter") -> None:
        """Display the map in a browser.

        Returns
        -------
        None

        """
        return self._map.show_in_browser()
