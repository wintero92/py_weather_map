from pathlib import Path

import pytest
from shapely.geometry import MultiPolygon
from shapely.wkt import loads as wkt_loads

# D103 Missing docstring in public function

# ruff: noqa: D103


@pytest.fixture(name="multipolygon_sicily")
def fixture_multipolygon_sicily() -> MultiPolygon:
    with Path.open(
        Path("test/unit/adapter/osmnx_adapter/data", "multipolygon_sicily.wkt"),
    ) as file:
        multipolygon_wkt = file.read()
        return wkt_loads(multipolygon_wkt)
