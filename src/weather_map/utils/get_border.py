import osmnx
import folium
from shapely.geometry import Polygon, MultiPolygon
from weather_map.utils.nominatim import Nominatim


def fetch_border(place_name: Nominatim) -> MultiPolygon | Polygon:
    gdf = osmnx.geocode_to_gdf(place_name)
    border = gdf.loc[0, "geometry"]
    return border


border = fetch_border(Nominatim.ITALY)
print(type(border))
a = border.geoms[0].exterior.coords
print(type(a))
print(a[0][0])
print(a[0])




# Initialize the map centered around Italy
# map_center = [41.8719, 12.5674]  # Center of Italy
# mymap = folium.Map(location=map_center, zoom_start=1, tiles="OpenStreetMap")


# Function to convert shapely geometry to GeoJSON format
def shapely_to_geojson(geometry):
    if isinstance(geometry, Polygon):
        return {
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": [list(geometry.exterior.coords)],
            },
            "properties": {},
        }
    elif isinstance(geometry, MultiPolygon):
        return {
            "type": "Feature",
            "geometry": {
                "type": "MultiPolygon",
                "coordinates": [
                    [list(poly.exterior.coords)] for poly in geometry.geoms
                ],
            },
            "properties": {},
        }


# Convert the Italy border to GeoJSON
# italy_geojson = shapely_to_geojson(italy_border)

# Add the Italy border to the map
# folium.GeoJson(
#    italy_geojson,
#    style_function=lambda x: {"color": "blue", "weight": 2, "fillOpacity": 0.1},
# ).add_to(mymap)

# Save the map to an HTML file
# mymap.save("italy_border_map.html")

# Display the map in a Jupyter Notebook (optional)
# from IPython.display import IFrame
# IFrame("italy_border_map.html", width=700, height=500)
