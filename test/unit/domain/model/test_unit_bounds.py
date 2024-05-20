import pytest
from shapely.geometry.polygon import Polygon
from weather_map.domain.model.bounds import Bounds, bounds_factory


def test_bounds_factory_from_shapely(shapely_polygon: Polygon) -> None:
    result = bounds_factory(input=shapely_polygon)

    isinstance(result, Bounds)
    assert result.min_x == shapely_polygon.bounds[0]
    assert result.min_y == shapely_polygon.bounds[1]
    assert result.max_x == shapely_polygon.bounds[2]
    assert result.max_y == shapely_polygon.bounds[3]


def test_bounds_factory_not_known_input() -> None:
    with pytest.raises(NotImplementedError):
        bounds_factory(input="not_known_input")
