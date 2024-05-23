import pytest
from weather_map.adapter.osmnx_adapter.osmnx_adapter import OsmnxAdapter
from weather_map.domain.model.location import Coordinate, Location


@pytest.fixture(name="location_sicily")
def fixture_location_sicily() -> Location:
    return Location(
        address="Sicilia, Italia",
        coordiante=Coordinate(latitude=37.587794, longitude=14.155048),
    )


@pytest.fixture(name="osmnx_instance")
def fixture_osmnx_instance() -> OsmnxAdapter:
    return OsmnxAdapter()
