from math import floor

from pyproj import Proj, Transformer
from shapely.geometry import MultiPolygon, Polygon


def _get_utm_zone(longitude: float, latitude: float) -> str:
    """Calculate the EPSG code for the UTM zone corresponding to the given longitude and
    latitude.

    Parameters
    ----------
    longitude : float
        The longitude of the point.
    latitude : float
        The latitude of the point.

    Returns
    -------
    str
        The EPSG code as a string.

    """
    zone_number = floor((longitude + 180) / 6) + 1
    epsg_code = 32600 + zone_number if latitude >= 0 else 32700 + zone_number
    return str(epsg_code)


def _transform_polygon_to_utm(polygon: Polygon, epsg_code: str) -> Polygon:
    """Transform a polygon to UTM coordinates.

    Parameters
    ----------
    polygon : Polygon
        The Shapely polygon to transform.
    epsg_code : str
        The EPSG code for the target UTM zone.

    Returns
    -------
    Polygon
        The transformed polygon.

    """
    input_proj = Proj("epsg:4326")  # WGS84 coordinate system
    output_proj = Proj(f"epsg:{epsg_code}")  # Target UTM coordinate system
    transformer = Transformer.from_proj(input_proj, output_proj, always_xy=True)

    transformed_coords = [
        transformer.transform(x, y) for x, y in polygon.exterior.coords
    ]
    return Polygon(transformed_coords)


def _transform_multipolygon_to_utm(
    multipolygon: MultiPolygon,
    epsg_code: str,
) -> MultiPolygon:
    """Transform a multipolygon to UTM coordinates.

    Parameters
    ----------
    multipolygon : MultiPolygon
        The Shapely multipolygon to transform.
    epsg_code : str
        The EPSG code for the target UTM zone.

    Returns
    -------
    MultiPolygon
        The transformed multipolygon.

    """
    transformed_polygons = [
        _transform_polygon_to_utm(polygon, epsg_code) for polygon in multipolygon.geoms
    ]
    return MultiPolygon(transformed_polygons)


def compute_area(geometry: Polygon | MultiPolygon) -> float:
    """Compute the area of a geometry (Polygon or MultiPolygon) in square meters.

    Parameters
    ----------
    geometry : Polygon or MultiPolygon
        The Shapely geometry whose area is to be computed. Can be a Polygon or MultiPolygon.

    Returns
    -------
    float
        The area of the geometry in square meters.

    """
    if not isinstance(geometry, Polygon | MultiPolygon):
        raise NotImplementedError

    centroid = geometry.centroid
    longitude, latitude = centroid.x, centroid.y

    epsg = _get_utm_zone(longitude=longitude, latitude=latitude)

    if isinstance(geometry, Polygon):
        transformed_geometry = _transform_polygon_to_utm(geometry, epsg_code=epsg)
    else:
        transformed_geometry = _transform_multipolygon_to_utm(geometry, epsg_code=epsg)

    return transformed_geometry.area
