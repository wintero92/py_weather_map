from shapely.geometry import MultiPolygon, Polygon
from weather_map.adapter.osmnx_adapter.transform import _transform_multipolygon_to_utm

# D103 Missing docstring in public function
# S101 Use of `assert` detected

# ruff: noqa: D103
# ruff: noqa: S101


def test_transform_multipolygon_to_utm() -> None:
    polygon1 = Polygon(
        [(-75.0, 40.0), (-75.0, 41.0), (-74.0, 41.0), (-74.0, 40.0), (-75.0, 40.0)],
    )
    polygon2 = Polygon(
        [(-76.0, 39.0), (-76.0, 40.0), (-75.0, 40.0), (-75.0, 39.0), (-76.0, 39.0)],
    )
    multipolygon = MultiPolygon([polygon1, polygon2])

    epsg_code = "32618"  # Example EPSG code for UTM zone 18N
    transformed_multipolygon = _transform_multipolygon_to_utm(multipolygon, epsg_code)

    assert transformed_multipolygon.is_valid
    assert len(transformed_multipolygon.geoms) == len(multipolygon.geoms)
    for original_polygon, transformed_polygon in zip(
        multipolygon.geoms,
        transformed_multipolygon.geoms,
        strict=False,
    ):
        assert transformed_polygon.is_valid
        assert len(transformed_polygon.exterior.coords) == len(
            original_polygon.exterior.coords,
        )
        for original_coord, transformed_coord in zip(
            original_polygon.exterior.coords,
            transformed_polygon.exterior.coords,
            strict=False,
        ):
            assert original_coord != transformed_coord
        assert (
            transformed_polygon.exterior.coords[0]
            == transformed_polygon.exterior.coords[-1]
        )
