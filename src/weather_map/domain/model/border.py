from pydantic import BaseModel
from weather_map.domain.model.bounds import Bounds
from weather_map.domain.model.coordinate import Coordinate
from weather_map.domain.model.polygon import Polygon


class Border(BaseModel):
    """Border class represents a geographical border with specific attributes.

    Attributes
    ----------
        area (float): The area of the border.
        bounds (Bounds): The bounding box or geographical bounds of the border.
        centroid (Coordinate): The geometric center of the border.
        polygons (list[Polygon]): A list of polygons that define the border.

    """

    area: float
    bounds: Bounds
    centroid: Coordinate
    polygons: list[Polygon]
