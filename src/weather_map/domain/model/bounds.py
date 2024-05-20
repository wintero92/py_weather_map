from pydantic import BaseModel

from shapely.geometry.polygon import Polygon
from shapely.geometry.multipolygon import MultiPolygon


class Bounds(BaseModel):
    min_x: float
    min_y: float
    max_x: float
    max_y: float


def _shepely_polygon_to_bounds(shapely_object: Polygon | MultiPolygon) -> Bounds:
    raw = shapely_object.bounds

    min_x = raw[0]
    min_y = raw[1]
    max_x = raw[2]
    max_y = raw[3]

    return Bounds(min_x=min_x, min_y=min_y, max_x=max_x, max_y=max_y)


def bounds_factory(input: Polygon) -> Bounds:
    if isinstance(input, Polygon) or isinstance(input, MultiPolygon):
        return _shepely_polygon_to_bounds(shapely_object=input)
    else:
        raise NotImplementedError
