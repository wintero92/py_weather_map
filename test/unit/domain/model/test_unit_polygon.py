import pytest
from shapely.geometry.polygon import Polygon as ShapelyPolygon
from weather_map.domain.model.polygon import Polygon, polygon_factory

# S101 Use of `assert` detected
# ruff: noqa: S101


def test_bounds_factory_from_shapely(shapely_polygon: ShapelyPolygon) -> None:
    result = polygon_factory(input=shapely_polygon)

    isinstance(result, Polygon)

    assert result.area == shapely_polygon.area

    assert result.centroid[0] == shapely_polygon.centroid.x
    assert result.centroid[1] == shapely_polygon.centroid.y

    assert result.bounds.min_x == shapely_polygon.bounds[0]
    assert result.bounds.min_y == shapely_polygon.bounds[1]
    assert result.bounds.max_x == shapely_polygon.bounds[2]
    assert result.bounds.max_y == shapely_polygon.bounds[3]

    assert result.longitude == [
        coordinate[0] for coordinate in shapely_polygon.exterior.coords
    ]
    assert result.latitude == [
        coordinate[1] for coordinate in shapely_polygon.exterior.coords
    ]


def test_bounds_factory_not_known_input() -> None:
    with pytest.raises(NotImplementedError):
        polygon_factory(input="not_known_input")
