from math import isclose

from weather_map.adapter.osmnx_adapter.osmnx_adapter import OsmnxAdapter
from weather_map.domain.model.border import Border
from weather_map.domain.model.location import Location

# D103 Missing docstring in public function
# S101 Use of `assert` detected

# ruff: noqa: D103
# ruff: noqa: S101


def test_compute_border(
    osmnx_instance: OsmnxAdapter,
    location_sicily: Location,
) -> None:
    border = osmnx_instance.compute_border(location=location_sicily)

    assert isinstance(border, Border)

    expected_area = 25711000000
    assert isclose(border.area, expected_area, rel_tol=10000000)
