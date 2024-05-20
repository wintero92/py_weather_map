from pydantic import BaseModel
from weather_map.domain.model.bounds import Bounds, bounds_factory

from shapely.geometry.polygon import Polygon as ShapelyPolygon


class Polygon(BaseModel):
    longitude: list[float]
    latitude: list[float]
    area: float
    centroid: tuple[float, float]
    bounds: Bounds


def _shepely_to_polygon(shapely_polygon: ShapelyPolygon) -> Polygon:
    area: float = shapely_polygon.area
    centroid: tuple[float, float] = (
        shapely_polygon.centroid.y,
        shapely_polygon.centroid.x,
    )
    bounds: Bounds = bounds_factory(input=shapely_polygon)

    longitude: list[float] = []
    latitude: list[float] = []

    for coordinate in shapely_polygon.exterior.coords:
        longitude.append(coordinate[0])
        latitude.append(coordinate[1])

    return Polygon(
        longitude=longitude,
        latitude=latitude,
        area=area,
        centroid=centroid,
        bounds=bounds,
    )


def polygon_factory(input: ShapelyPolygon) -> Polygon:
    if isinstance(input, ShapelyPolygon):
        return _shepely_to_polygon(shapely_polygon=input)
    else:
        raise NotImplementedError
