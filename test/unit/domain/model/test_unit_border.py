import pytest
from shapely.geometry.polygon import Polygon as ShapelyPolygon
from shapely.geometry.multipolygon import MultiPolygon as ShapelyMultiPolygon
from weather_map.domain.model.bounds import Bounds
from weather_map.domain.model.polygon import Polygon, polygon_factory
from weather_map.domain.model.border import Border, border_factory


def test_border_factory_from_shapely_polygon(shapely_polygon: ShapelyPolygon) -> None:
    result = border_factory(input=shapely_polygon)

    isinstance(result, Border)

    assert result.area == shapely_polygon.area

    assert result.centroid[0] == shapely_polygon.centroid.y
    assert result.centroid[1] == shapely_polygon.centroid.x

    assert result.bounds.min_x == shapely_polygon.bounds[0]
    assert result.bounds.min_y == shapely_polygon.bounds[1]
    assert result.bounds.max_x == shapely_polygon.bounds[2]
    assert result.bounds.max_y == shapely_polygon.bounds[3]

    assert result.polygons[0].longitude == [
        coordinate[0] for coordinate in shapely_polygon.exterior.coords
    ]
    assert result.polygons[0].latitude == [
        coordinate[1] for coordinate in shapely_polygon.exterior.coords
    ]

    assert result.polygons[0].area == shapely_polygon.area

    assert result.polygons[0].centroid[0] == shapely_polygon.centroid.x
    assert result.polygons[0].centroid[1] == shapely_polygon.centroid.y

    assert result.polygons[0].bounds.min_x == shapely_polygon.bounds[0]
    assert result.polygons[0].bounds.min_y == shapely_polygon.bounds[1]
    assert result.polygons[0].bounds.max_x == shapely_polygon.bounds[2]
    assert result.polygons[0].bounds.max_y == shapely_polygon.bounds[3]


def test_border_factory_from_shapely_multi_polygon(
    shapely_multi_polygon: ShapelyMultiPolygon,
) -> None:
    result = border_factory(input=shapely_multi_polygon)

    isinstance(result, Border)

    assert result.area == shapely_multi_polygon.area

    assert result.centroid[0] == shapely_multi_polygon.centroid.y
    assert result.centroid[1] == shapely_multi_polygon.centroid.x

    assert result.bounds.min_x == shapely_multi_polygon.bounds[0]
    assert result.bounds.min_y == shapely_multi_polygon.bounds[1]
    assert result.bounds.max_x == shapely_multi_polygon.bounds[2]
    assert result.bounds.max_y == shapely_multi_polygon.bounds[3]

    assert result.polygons[0].longitude == [
        coordinate[0] for coordinate in shapely_multi_polygon.geoms[0].exterior.coords
    ]
    assert result.polygons[0].latitude == [
        coordinate[1] for coordinate in shapely_multi_polygon.geoms[0].exterior.coords
    ]

    assert result.polygons[0].area == shapely_multi_polygon.geoms[0].area

    assert result.polygons[0].centroid[0] == shapely_multi_polygon.geoms[0].centroid.y
    assert result.polygons[0].centroid[1] == shapely_multi_polygon.geoms[0].centroid.x

    assert result.polygons[0].bounds.min_x == shapely_multi_polygon.geoms[0].bounds[0]
    assert result.polygons[0].bounds.min_y == shapely_multi_polygon.geoms[0].bounds[1]
    assert result.polygons[0].bounds.max_x == shapely_multi_polygon.geoms[0].bounds[2]
    assert result.polygons[0].bounds.max_y == shapely_multi_polygon.geoms[0].bounds[3]

    assert result.polygons[1].longitude == [
        coordinate[0] for coordinate in shapely_multi_polygon.geoms[1].exterior.coords
    ]
    assert result.polygons[1].latitude == [
        coordinate[1] for coordinate in shapely_multi_polygon.geoms[1].exterior.coords
    ]

    assert result.polygons[1].area == shapely_multi_polygon.geoms[1].area

    assert result.polygons[1].centroid[0] == shapely_multi_polygon.geoms[1].centroid.y
    assert result.polygons[1].centroid[1] == shapely_multi_polygon.geoms[1].centroid.x

    assert result.polygons[1].bounds.min_x == shapely_multi_polygon.geoms[1].bounds[0]
    assert result.polygons[1].bounds.min_y == shapely_multi_polygon.geoms[1].bounds[1]
    assert result.polygons[1].bounds.max_x == shapely_multi_polygon.geoms[1].bounds[2]
    assert result.polygons[1].bounds.max_y == shapely_multi_polygon.geoms[1].bounds[3]


def test_border_factory_not_known_input() -> None:
    with pytest.raises(NotImplementedError):
        border_factory(input="not_known_input")
