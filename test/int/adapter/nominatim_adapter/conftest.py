import pytest
from weather_map.adapter.nominatim_adapter.nominatim_adapter import NominatimAdapter


@pytest.fixture(name="nominatim_instance")
def fixture_nominatim_instance() -> NominatimAdapter:
    return NominatimAdapter()
