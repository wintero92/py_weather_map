from pydantic import BaseModel, Field


class Coordinate(BaseModel):

    """A model representing geographic coordinates with latitude and longitude.

    This model uses Pydantic for data validation and ensures that the latitude
    and longitude values are within their respective valid ranges.

    Attributes
    ----------
    - latitude (float): The latitude of the coordinate, must be between -90 and 90.
    - longitude (float): The longitude of the coordinate, must be between -180 and 180.

    """

    latitude: float = Field(
        ...,
        ge=-90,
        le=90,
        description="Latitude must be between -90 and 90",
    )
    longitude: float = Field(
        ...,
        ge=-180,
        le=180,
        description="Longitude must be between -180 and 180",
    )
