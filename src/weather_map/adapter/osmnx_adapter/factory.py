from shapely.geometry.multipolygon import MultiPolygon as ShapelyMultiPolygon
from shapely.geometry.polygon import Polygon as ShapelyPolygon
from weather_map.adapter.osmnx_adapter.transform import compute_area
from weather_map.domain.model.border import Border
from weather_map.domain.model.bounds import Bounds
from weather_map.domain.model.coordinate import Coordinate
from weather_map.domain.model.polygon import Polygon


def _shapely_polygon_to_bounds(
    *,
    geometry: ShapelyPolygon | ShapelyMultiPolygon,
) -> Bounds:
    """Convert a Shapely polygon or multipolygon to Bounds.

    Args:
    ----
        geometry (ShapelyPolygon | ShapelyMultiPolygon): The Shapely geometry object.

    Returns:
    -------
        Bounds: The bounding coordinates of the geometry.

    """
    bounds = geometry.bounds
    return Bounds(
        min=Coordinate(latitude=bounds[1], longitude=bounds[0]),
        max=Coordinate(latitude=bounds[3], longitude=bounds[2]),
    )


def _shapely_polygon_to_centroid(
    *,
    geometry: ShapelyPolygon | ShapelyMultiPolygon,
) -> Coordinate:
    """Compute the centroid of a Shapely polygon or multipolygon.

    Args:
    ----
        geometry (ShapelyPolygon | ShapelyMultiPolygon): The Shapely geometry object.

    Returns:
    -------
        Coordinate: The centroid of the geometry.

    """
    return Coordinate(
        longitude=geometry.centroid.x,
        latitude=geometry.centroid.y,
    )


def _shapely_single_polygon_to_polygon(*, shapely_polygon: ShapelyPolygon) -> Polygon:
    """Convert a single Shapely polygon to a Polygon domain model.

    Args:
    ----
        shapely_polygon (ShapelyPolygon): The Shapely polygon object.

    Returns:
    -------
        Polygon: The domain model Polygon.

    """
    area = compute_area(geometry=shapely_polygon)
    centroid = _shapely_polygon_to_centroid(geometry=shapely_polygon)
    bounds = _shapely_polygon_to_bounds(geometry=shapely_polygon)
    coordinates: list[Coordinate] = [
        Coordinate(longitude=coord[0], latitude=coord[1])
        for coord in shapely_polygon.exterior.coords
    ]

    return Polygon(
        area=area,
        bounds=bounds,
        centroid=centroid,
        coordinates=coordinates,
    )


def _shapely_single_polygon_to_border(*, shapely_polygon: ShapelyPolygon) -> Border:
    """Convert a single Shapely polygon to a Border domain model.

    Args:
    ----
        shapely_polygon (ShapelyPolygon): The Shapely polygon object.

    Returns:
    -------
        Border: The domain model Border.

    """
    polygon = _shapely_single_polygon_to_polygon(shapely_polygon=shapely_polygon)

    return Border(
        area=polygon.area,
        bounds=polygon.bounds,
        centroid=polygon.centroid,
        polygons=[polygon],
    )


def _shapely_multi_polygon_to_border(
    *,
    shapely_multi_polygon: ShapelyMultiPolygon,
) -> Border:
    """Convert a Shapely multipolygon to a Border domain model.

    Args:
    ----
        shapely_multi_polygon (ShapelyMultiPolygon): The Shapely multipolygon object.

    Returns:
    -------
        Border: The domain model Border.

    """
    area = compute_area(geometry=shapely_multi_polygon)
    centroid = _shapely_polygon_to_centroid(geometry=shapely_multi_polygon)
    bounds = _shapely_polygon_to_bounds(geometry=shapely_multi_polygon)

    polygons = [
        _shapely_single_polygon_to_polygon(shapely_polygon=shapely_polygon)
        for shapely_polygon in shapely_multi_polygon.geoms
    ]

    return Border(
        area=area,
        bounds=bounds,
        centroid=centroid,
        polygons=polygons,
    )


def shapely_to_border(geometry: ShapelyPolygon | ShapelyMultiPolygon) -> Border:
    """Convert Shapely polygon or multipolygon to a Border domain model.

    Args:
    ----
        geometry (ShapelyPolygon | ShapelyMultiPolygon): The Shapely geometry object.

    Returns:
    -------
        Border: The domain model Border.

    Raises:
    ------
        NotImplementedError: If the input type is not supported.

    """
    if not isinstance(geometry, ShapelyPolygon | ShapelyMultiPolygon):
        raise NotImplementedError

    if isinstance(geometry, ShapelyPolygon):
        return _shapely_single_polygon_to_border(shapely_polygon=geometry)
    return _shapely_multi_polygon_to_border(shapely_multi_polygon=geometry)
