from weather_map.adapter.osmnx_adapter.osmnx_adapter import OsmnxAdapter
from weather_map.domain.model.border import Border
from weather_map.domain.model.location import Location


def test_compute_border(
    osmnx_instance: OsmnxAdapter,
    location_sicily: Location,
) -> None:
    border = osmnx_instance.compute_border(location=location_sicily)

    assert isinstance(border, Border)
    print(border.area)
    print(len(border.polygons))
    print(border.polygons[0].area)
