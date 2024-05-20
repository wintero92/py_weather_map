import geopandas as gpd
import osmnx as ox
from shapely.geometry import Polygon, MultiPolygon, Point
from shapely.ops import unary_union
import numpy as np
import pandas as pd
from scipy.spatial import Delaunay
import folium
from folium.plugins import HeatMap

# Constants
MILE_IN_KM = 1.60934
BUFFER_DISTANCE = MILE_IN_KM  # 1 mile buffer into the sea

# Get the border and coastline data for Italy
gdf = ox.geometries_from_place("Italy", {"boundary": "administrative"})
coastline = ox.geometries_from_place("Italy", {"natural": "coastline"})

# Extract the polygon of Italy's border
italy_border = gdf[gdf["admin_level"] == "2"].geometry.unary_union

# Buffer the coastline 1 mile into the sea
extended_coastline = coastline.geometry.buffer(BUFFER_DISTANCE)

# Combine the Italy border with the extended coastline
combined_geometry = italy_border.union(unary_union(extended_coastline))

# Ensure the result is a MultiPolygon for consistent handling
if combined_geometry.type == "Polygon":
    combined_geometry = MultiPolygon([combined_geometry])

# Generate synthetic GPS data points within the extended border
minx, miny, maxx, maxy = combined_geometry.bounds
num_points = 100  # Number of synthetic data points

points = []
while len(points) < num_points:
    random_point = Point(np.random.uniform(minx, maxx), np.random.uniform(miny, maxy))
    if combined_geometry.contains(random_point):
        points.append((random_point.y, random_point.x))

gps_data = pd.DataFrame(points, columns=["latitude", "longitude"])
temperatures = np.random.uniform(10, 30, num_points)  # Synthetic temperature data
weather_data = gps_data.copy()
weather_data["temperature"] = temperatures

# Perform Delaunay triangulation
triangulation = Delaunay(weather_data[["latitude", "longitude"]].values)


# Function to convert Delaunay triangles to GeoJSON format
def triangles_to_geojson(points, triangles):
    geojson = {"type": "FeatureCollection", "features": []}
    for triangle in triangles:
        coordinates = [[points[i][1], points[i][0]] for i in triangle]
        coordinates.append(coordinates[0])  # Close the polygon
        feature = {
            "type": "Feature",
            "geometry": {"type": "Polygon", "coordinates": [coordinates]},
            "properties": {},
        }
        geojson["features"].append(feature)
    return geojson


# Convert triangulation to GeoJSON
triangles_geojson = triangles_to_geojson(
    weather_data[["latitude", "longitude"]].values, triangulation.simplices
)

# Initialize the map centered around Italy
map_center = [41.8719, 12.5674]  # Center of Italy
mymap = folium.Map(location=map_center, zoom_start=6, tiles="OpenStreetMap")

# Add triangulated mesh to the map
folium.GeoJson(
    triangles_geojson,
    style_function=lambda x: {"color": "blue", "weight": 1, "fillOpacity": 0.1},
).add_to(mymap)

# Add markers for the GPS coordinates
for _, row in gps_data.iterrows():
    folium.Marker([row["latitude"], row["longitude"]]).add_to(mymap)

# Save the map to an HTML file
mymap.save("triangulated_map_italy.html")
