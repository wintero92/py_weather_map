from pydantic import BaseModel
from weather_map.domain.model.bounds import Bounds
from weather_map.domain.model.coordinate import Coordinate


class Polygon(BaseModel):

    """Polygon class represents a geographical polygon with specific attributes.

    Attributes
    ----------
        area (float): The area of the polygon.
        bounds (Bounds): The bounding box or geographical bounds of the polygon.
        centroid (Coordinate): The geometric center of the polygon.
        coordinates (list[Coordinate]): A list of coordinates that define the vertices of the polygon.

    """

    area: float
    bounds: Bounds
    centroid: Coordinate
    coordinates: list[Coordinate]
