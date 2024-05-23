from weather_map.adapter.osmnx_adapter.transform import _get_utm_zone

# D103 Missing docstring in public function
# S101 Use of `assert` detected

# ruff: noqa: D103
# ruff: noqa: S101


def test_get_utm_zone_northern_hemisphere() -> None:
    assert _get_utm_zone(-75.0, 40.0) == "32618"


def test_get_utm_zone_southern_hemisphere() -> None:
    assert _get_utm_zone(-75.0, -40.0) == "32718"


def test_get_utm_zone_equator() -> None:
    assert _get_utm_zone(0.0, 0.0) == "32631"


def test_get_utm_zone_negative_longitude() -> None:
    assert _get_utm_zone(-180.0, 0.0) == "32601"


def test_get_utm_zone_positive_longitude() -> None:
    assert _get_utm_zone(179.9, 0.0) == "32660"


def test_get_utm_zone_high_latitude_north() -> None:
    assert _get_utm_zone(0.0, 84.0) == "32631"


def test_get_utm_zone_high_latitude_south() -> None:
    assert _get_utm_zone(0.0, -80.0) == "32731"
