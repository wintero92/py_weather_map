import folium
import pandas as pd
from scipy.spatial import Delaunay

# Load the synthetic data
gps_data = pd.read_csv("gps_coordinates_italy.csv")
weather_data = pd.read_csv("weather_data_italy.csv")

# Perform Delaunay triangulation
points = weather_data[["latitude", "longitude"]].values
triangulation = Delaunay(points)

# Initialize the map centered around Italy
map_center = [41.8719, 12.5674]  # Center of Italy
mymap = folium.Map(location=map_center, zoom_start=6, tiles="OpenStreetMap")


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
triangles_geojson = triangles_to_geojson(points, triangulation.simplices)

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
