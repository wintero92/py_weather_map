from math import isclose

import pytest
from shapely.geometry import MultiPolygon
from weather_map.adapter.osmnx_adapter.transform import compute_area

# D103 Missing docstring in public function
# S101 Use of `assert` detected

# ruff: noqa: D103
# ruff: noqa: S101


def test_compute_area_polygon(multipolygon_sicily: MultiPolygon) -> None:
    polygon = multipolygon_sicily.geoms[0]

    area = compute_area(polygon)

    expected_area = 25711000000
    assert isclose(area, expected_area, rel_tol=10000000)


def test_compute_area_multipolygon(multipolygon_sicily: MultiPolygon) -> None:
    area = compute_area(multipolygon_sicily)

    expected_area = 25711000000
    assert isclose(area, expected_area, rel_tol=10000000)


def test_compute_area_unknown() -> None:
    with pytest.raises(NotImplementedError):
        compute_area("unknown")
