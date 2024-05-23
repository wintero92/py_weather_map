from shapely.geometry import Polygon
from weather_map.adapter.osmnx_adapter.transform import _transform_polygon_to_utm

# D103 Missing docstring in public function
# S101 Use of `assert` detected

# ruff: noqa: D103
# ruff: noqa: S101


def test_transform_polygon_to_utm() -> None:
    polygon = Polygon(
        [(-75.0, 40.0), (-75.0, 41.0), (-74.0, 41.0), (-74.0, 40.0), (-75.0, 40.0)],
    )

    epsg_code = "32618"  # Example EPSG code for UTM zone 18N
    transformed_polygon = _transform_polygon_to_utm(polygon, epsg_code)

    assert transformed_polygon.is_valid
    assert len(transformed_polygon.exterior.coords) == len(polygon.exterior.coords)
    for original_coord, transformed_coord in zip(
        polygon.exterior.coords,
        transformed_polygon.exterior.coords,
        strict=False,
    ):
        assert original_coord != transformed_coord
    assert (
        transformed_polygon.exterior.coords[0]
        == transformed_polygon.exterior.coords[-1]
    )
