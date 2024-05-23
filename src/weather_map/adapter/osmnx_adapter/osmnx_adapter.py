import osmnx
from weather_map.domain.model.border import Border, border_factory
from weather_map.domain.model.location import Location
from weather_map.port.compute_border import ComputeBorder


class OsmnxAdapter(ComputeBorder):

    def _compute_border(self, *, location: Location) -> Border:
        gdf = osmnx.geocode_to_gdf(location.address)
        shapely_object = gdf.loc[0, "geometry"]

        return border_factory(input=shapely_object)
