from pydantic import BaseModel
from weather_map.domain.model.coordinate import Coordinate


class Location(BaseModel):

    """Location domain model class."""

    address: str
    coordiante: Coordinate
