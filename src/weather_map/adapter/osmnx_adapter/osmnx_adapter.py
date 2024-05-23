import osmnx
from weather_map.adapter.osmnx_adapter.factory import shapely_to_border
from weather_map.domain.model.border import Border
from weather_map.domain.model.location import Location
from weather_map.port.compute_border import ComputeBorder


class OsmnxAdapter(ComputeBorder):
    """OsmnxAdapter is an adapter class that uses the osmnx library to compute the
    border of a given location.

    Methods
    -------
        _compute_border(location: Location) -> Border:
            Computes the border of the given location using osmnx and converts it to a Border object.

    """

    def _compute_border(self: "OsmnxAdapter", *, location: Location) -> Border:
        """Compute the border for a given Location instance using osmnx.

        Args:
        ----
            location (Location): The Location instance to compute the border from.

        Returns:
        -------
            Border: A Border instance computed from the Location data using osmnx.

        This method geocodes the address from the Location object to a GeoDataFrame, extracts the geometry,
        and converts it to a Border object using the shapely_to_border function.

        """
        gdf = osmnx.geocode_to_gdf(location.address)
        shapely_object = gdf.loc[0, "geometry"]
        return shapely_to_border(geometry=shapely_object)
