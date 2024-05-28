from pydantic import BaseModel
from weather_map.domain.model.coordinate import Coordinate


class Location(BaseModel):

    """Location domain model class.

    Attributes
    ----------
        address (str): The address of the location.
        coordinate (Coordinate): The geographical coordinate of the location.

    """

    address: str
    coordinate: Coordinate
