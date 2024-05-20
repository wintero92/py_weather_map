from weather_map.domain.model.border import Border
from weather_map.domain.model.nominatim import Nominatim
from weather_map.port.compute_border import ComputeBorder
import osmnx
from weather_map.domain.model.border import border_factory


class OsmnxComputeBorderAdapter(ComputeBorder):

    def _compute_border(self, *, nominatim: Nominatim) -> Border:
        gdf = osmnx.geocode_to_gdf(nominatim.value)
        shapely_object = gdf.loc[0, "geometry"]

        return border_factory(input=shapely_object)
