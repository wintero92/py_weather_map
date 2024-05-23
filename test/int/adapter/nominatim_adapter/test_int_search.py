from weather_map.adapter.nominatim_adapter.nominatim_adapter import NominatimAdapter
from weather_map.domain.model.location import Location


def test_search(nominatim_instance: NominatimAdapter) -> None:
    location = nominatim_instance.search(search_pattern="Sicily")

    assert isinstance(location, Location)
    location.address == "Sicilia, Italia"
