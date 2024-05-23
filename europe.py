import folium
import geopandas as gpd

# Load the naturalearth_lowres dataset
world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))

# Filter the dataset to include only European countries
europe = world[world["continent"] == "Europe"]

# List all European countries
european_countries = europe["name"].tolist()
print("European countries:")
for country in european_countries:
    print(country)

# Initialize the map centered around Europe
map_center = [54.5260, 15.2551]  # Roughly the center of Europe
mymap = folium.Map(location=map_center, zoom_start=4, tiles="OpenStreetMap")


# Function to convert GeoDataFrame to GeoJSON format
def gdf_to_geojson(gdf):
    return gdf.__geo_interface__


# Convert the European countries GeoDataFrame to GeoJSON
europe_geojson = gdf_to_geojson(europe)

# Add the European countries boundaries to the map
folium.GeoJson(
    europe_geojson,
    style_function=lambda x: {"color": "blue", "weight": 2, "fillOpacity": 0.1},
).add_to(mymap)

# Save the map to an HTML file
mymap.save("europe_countries_map.html")

# Display the map in a Jupyter Notebook (optional)
# from IPython.display import IFrame
# IFrame("europe_countries_map.html", width=700, height=500)
