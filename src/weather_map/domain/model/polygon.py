from pydantic import BaseModel
from shapely.geometry.polygon import Polygon as ShapelyPolygon
from weather_map.domain.model.bounds import Bounds, bounds_factory
from weather_map.domain.model.coordinate import Coordinate


class Polygon(BaseModel):
    area: float
    bounds: Bounds
    centroid: Coordinate
    coordinates: list[Coordinate]


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
