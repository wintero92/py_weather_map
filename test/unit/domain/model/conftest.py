import pytest
from shapely.geometry.multipolygon import MultiPolygon
from shapely.geometry.polygon import Polygon


@pytest.fixture(name="shapely_polygon")
def fixture_shapely_polygon() -> Polygon:
    return Polygon(((0.0, 0.0), (0.0, 1.0), (1.0, 1.0), (1.0, 0.0), (0.0, 0.0)))


@pytest.fixture(name="shapely_multi_polygon")
def fixture_shapely_multi_polygon() -> MultiPolygon:
    return MultiPolygon(
        [
            Polygon(((1.0, 0.0), (1.0, 1.0), (2.0, 1.0), (2.0, 0.0), (1.0, 0.0))),
            Polygon(((3.0, 2.0), (3.0, 3.0), (4.0, 3.0), (4.0, 2.0), (3.0, 2.0))),
        ],
    )
