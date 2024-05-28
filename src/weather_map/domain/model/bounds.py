from pydantic import BaseModel
from weather_map.domain.model.coordinate import Coordinate


class Bounds(BaseModel):

    """A class to represent the geographical bounds defined by minimum and maximum
    coordinates.

    Attributes
    ----------
        min (Coordinate): The minimum coordinate (bottom-left corner) of the bounds.
        max (Coordinate): The maximum coordinate (top-right corner) of the bounds.

    """

    min: Coordinate
    max: Coordinate
