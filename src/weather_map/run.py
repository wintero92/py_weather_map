from weather_map.adapter.osmnx_compute_border_adapter.osmnx_compute_border_adapter import (
    OsmnxComputeBorderAdapter,
)
from weather_map.domain.model.nominatim import Nominatim
import folium

italy_border = OsmnxComputeBorderAdapter().compute_border(nominatim=Nominatim.ITALY)

mymap = folium.Map(
    location=italy_border.centroid,
    width=2000,
    height=2000,
    zoom_start=7,
    tiles="OpenStreetMap",
)

image = mymap._to_png()
with open("image.png", mode="bw") as file:
    file.write(image)
