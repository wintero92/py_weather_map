from weather_map.adapter.nominatim_adapter.nominatim_adapter import NominatimAdapter
from weather_map.domain.model.coordinate import Coordinate
from weather_map.domain.model.location import Location

# D103 Missing docstring in public function
# S101 Use of `assert` detected

# ruff: noqa: D103
# ruff: noqa: S101


def test_search(nominatim_instance: NominatimAdapter) -> None:
    location = nominatim_instance.search(search_pattern="Sicily")

    assert isinstance(location, Location)
    assert location.address == "Sicilia, Italia"
    assert location.coordinate == Coordinate(latitude=37.587794, longitude=14.155048)
