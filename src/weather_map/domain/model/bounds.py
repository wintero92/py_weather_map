from pydantic import BaseModel
from weather_map.domain.model.coordinate import Coordinate


class Bounds(BaseModel):
    min: Coordinate
    max: Coordinate
