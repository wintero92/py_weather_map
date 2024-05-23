from pydantic import BaseModel
from shapely.geometry.multipolygon import MultiPolygon as ShapelyMultiPolygon
from shapely.geometry.polygon import Polygon as ShapelyPolygon
from weather_map.domain.model.bounds import Bounds, bounds_factory
from weather_map.domain.model.polygon import Polygon, polygon_factory
from weather_map.domain.model.coordinate import Coordinate


class Border(BaseModel):
    area: float
    bounds: Bounds
    centroid: Coordinate
    polygons: list[Polygon]

    @property
    def geojson(self):
        return {
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    zip(polygon.longitude, polygon.latitude, strict=False)
                    for polygon in self.polygons
                ],
            },
            "properties": {},
        }


def _shapely_polygon_to_border(shapely_polygon: ShapelyPolygon) -> Border:
    polygon: Polygon = polygon_factory(input=shapely_polygon)

    polygons: list[Polygon] = [polygon]
    area: float = polygon.area
    centroid: tuple[float, float] = polygon.centroid
    bounds: Bounds = polygon.bounds

    return Border(polygons=polygons, area=area, centroid=centroid, bounds=bounds)


def _shapely_multi_polygon_to_border(
    shapely_multi_polygon: ShapelyMultiPolygon,
) -> Border:
    area: float = shapely_multi_polygon.area
    centroid: tuple[float, float] = (
        shapely_multi_polygon.centroid.y,
        shapely_multi_polygon.centroid.x,
    )
    bounds: Bounds = bounds_factory(input=shapely_multi_polygon)

    polygons: list[Polygon] = [
        polygon_factory(input=shapely_polygon)
        for shapely_polygon in shapely_multi_polygon.geoms
    ]

    return Border(polygons=polygons, area=area, centroid=centroid, bounds=bounds)


def border_factory(input: ShapelyPolygon) -> Border:
    if isinstance(input, ShapelyPolygon):
        return _shapely_polygon_to_border(shapely_polygon=input)
    elif isinstance(input, ShapelyMultiPolygon):
        return _shapely_multi_polygon_to_border(shapely_multi_polygon=input)
    else:
        raise NotImplementedError
