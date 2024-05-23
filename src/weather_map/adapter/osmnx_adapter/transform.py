from math import floor
from shapely.geometry import Polygon, MultiPolygon
from pyproj import Proj, transform


def _get_utm_zone(longitude: float, latitude: float) -> str:
    """
    Calculate the EPSG code for the UTM zone corresponding to the given longitude and latitude.

    Parameters:
    - longitude: The longitude of the point.
    - latitude: The latitude of the point.

    Returns:
    - EPSG code as a string.
    """
    zone_number = floor((longitude + 180) / 6) + 1
    if latitude >= 0:
        epsg_code = 32600 + zone_number
    else:
        epsg_code = 32700 + zone_number
    return str(epsg_code)


def _transform_polygon_to_utm(polygon: Polygon, epsg_code: str) -> Polygon:
    """
    Transform a polygon to UTM coordinates.

    Parameters:
    - polygon: The Shapely polygon to transform.
    - epsg_code: The EPSG code for the target UTM zone.

    Returns:
    - The transformed polygon.
    """
    input_proj = Proj("epsg:4326")  # WGS84
    output_proj = Proj(f"epsg:{epsg_code}")

    transformed_coords = [
        transform(input_proj, output_proj, x, y) for x, y in polygon.exterior.coords
    ]
    return Polygon(transformed_coords)


def _transform_multipolygon_to_utm(
    multipolygon: MultiPolygon, epsg_code: str
) -> MultiPolygon:
    """
    Transform a multipolygon to UTM coordinates.

    Parameters:
    - multipolygon: The Shapely multipolygon to transform.
    - epsg_code: The EPSG code for the target UTM zone.

    Returns:
    - The transformed multipolygon.
    """
    transformed_polygons = [
        _transform_polygon_to_utm(polygon, epsg_code) for polygon in multipolygon
    ]
    return MultiPolygon(transformed_polygons)


def compute_area(geometry) -> float:
    """
    Compute the area of a geometry (Polygon or MultiPolygon) in square meters.

    Parameters:
    - geometry: The Shapely geometry whose area is to be computed. Can be a Polygon or MultiPolygon.

    Returns:
    - The area of the geometry in square meters.
    """
    centroid = geometry.centroid
    longitude, latitude = centroid.x, centroid.y

    epsg = _get_utm_zone(longitude=longitude, latitude=latitude)

    if isinstance(geometry, Polygon):
        transformed_geometry = _transform_polygon_to_utm(geometry, epsg_code=epsg)
    elif isinstance(geometry, MultiPolygon):
        transformed_geometry = _transform_multipolygon_to_utm(geometry, epsg_code=epsg)
    else:
        raise ValueError("Geometry must be a Polygon or MultiPolygon")

    return transformed_geometry.area
