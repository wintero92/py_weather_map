import pandas as pd
import numpy as np
from scipy.interpolate import griddata
import folium
from folium.plugins import HeatMap

# Load the GPS coordinates and weather data
gps_data = pd.read_csv("gps_coordinates.csv")
weather_data = pd.read_csv("weather_data.csv")

# Extract coordinates and temperature values
points = weather_data[["latitude", "longitude"]].values
values = weather_data["temperature"].values

# Define a grid over the area of interest
grid_lat, grid_lon = np.mgrid[
    min(weather_data["latitude"]) : max(weather_data["latitude"]) : 100j,
    min(weather_data["longitude"]) : max(weather_data["longitude"]) : 100j,
]

# Interpolate the temperature values over the grid
grid_temperature = griddata(points, values, (grid_lat, grid_lon), method="cubic")

# Initialize the map centered around the average coordinates
map_center = [gps_data["latitude"].mean(), gps_data["longitude"].mean()]
mymap = folium.Map(location=map_center, zoom_start=5, tiles="OpenStreetMap")

# Prepare the interpolated data for heatmap
heat_data = np.vstack([grid_lat.ravel(), grid_lon.ravel(), grid_temperature.ravel()]).T
heat_data = heat_data[~np.isnan(heat_data[:, 2])]  # Remove NaN values

# Normalize the temperature values for heatmap
heat_data[:, 2] = (heat_data[:, 2] - heat_data[:, 2].min()) / (
    heat_data[:, 2].max() - heat_data[:, 2].min()
)

# Add the heatmap layer
HeatMap(heat_data, radius=10, blur=15, max_zoom=1).add_to(mymap)

# Add markers for the GPS coordinates
for _, row in gps_data.iterrows():
    folium.Marker([row["latitude"], row["longitude"]]).add_to(mymap)

# Save the map to an HTML file
mymap.save("heatmap.html")
