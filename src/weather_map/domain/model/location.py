from pydantic import BaseModel
from weather_map.domain.model.coordinate import Coordinate


class Location(BaseModel):
    address: str
    coordiante: Coordinate
