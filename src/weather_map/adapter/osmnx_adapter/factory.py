from shapely.geometry.multipolygon import MultiPolygon as ShapelyMultiPolygon
from shapely.geometry.polygon import Polygon as ShapelyPolygon
from weather_map.domain.model.bounds import Bounds
from weather_map.domain.model.polygon import Polygon
from weather_map.domain.model.border import Border
from weather_map.domain.model.coordinate import Coordinate
from weather_map.adapter.osmnx_adapter.transform import compute_area


def _shapely_polygon_to_bounds(
    *, shapely_polygon: ShapelyPolygon | ShapelyMultiPolygon
) -> Bounds:
    bounds = shapely_polygon.bounds
    return Bounds(
        min=Coordinate(latitude=bounds[1], longitude=bounds[0]),
        max=Coordinate(latitude=bounds[3], longitude=bounds[2]),
    )


def _shapely_single_polygon_to_polygon(shapely_polygon: ShapelyPolygon) -> Polygon:
    area = compute_area(geometry=shapely_polygon)
    centroid = Coordinate(
        longitude=shapely_polygon.centroid.x,
        latitude=shapely_polygon.centroid.y,
    )
    bounds: Bounds = _shapely_polygon_to_bounds(shapely_polygon=shapely_polygon)
    coordinates: list[Coordinate] = []
    for coordinate in shapely_polygon.exterior.coords:
        coordinates.append(Coordinate(longitude=coordinate[0], latitude=coordinate[1]))

    return Polygon(
        area=area,
        bounds=bounds,
        centroid=centroid,
        coordinates=coordinates,
    )


def _shapely_single_polygon_to_border(shapely_polygon: ShapelyPolygon) -> Border:
    polygon = _shapely_single_polygon_to_polygon(shapely_polygon=shapely_polygon)
    Border(
        area=polygon.area,
        bounds=polygon.bounds,
        centroid=polygon.centroid,
        polygons=[polygon],
    )


# def _shapely_polygon_to_border(shapely_polygon: ShapelyPolygon) -> Border:
#     polygon: Polygon = polygon_factory(input=shapely_polygon)

#     polygons: list[Polygon] = [polygon]
#     area: float = polygon.area
#     centroid: tuple[float, float] = polygon.centroid
#     bounds: Bounds = polygon.bounds

#     return Border(polygons=polygons, area=area, centroid=centroid, bounds=bounds)


# def _shapely_multi_polygon_to_border(
#     shapely_multi_polygon: ShapelyMultiPolygon,
# ) -> Border:
#     area: float = shapely_multi_polygon.area
#     centroid: tuple[float, float] = (
#         shapely_multi_polygon.centroid.y,
#         shapely_multi_polygon.centroid.x,
#     )
#     bounds: Bounds = bounds_factory(input=shapely_multi_polygon)

#     polygons: list[Polygon] = [
#         polygon_factory(input=shapely_polygon)
#         for shapely_polygon in shapely_multi_polygon.geoms
#     ]

#     return Border(polygons=polygons, area=area, centroid=centroid, bounds=bounds)


# def border_factory(input: ShapelyPolygon) -> Border:
#     if isinstance(input, ShapelyPolygon):
#         return _shapely_polygon_to_border(shapely_polygon=input)
#     elif isinstance(input, ShapelyMultiPolygon):
#         return _shapely_multi_polygon_to_border(shapely_multi_polygon=input)
#     else:
#         raise NotImplementedError
