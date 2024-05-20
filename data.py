import numpy as np
import pandas as pd

# Generate synthetic GPS data (latitude and longitude within Italy's bounding box)
np.random.seed(42)
latitudes = np.random.uniform(36.5, 47.0, 100)  # Latitude range for Italy
longitudes = np.random.uniform(6.6, 18.9, 100)  # Longitude range for Italy
temperatures = np.random.uniform(10, 30, 100)  # Synthetic temperature data

# Create a DataFrame for the synthetic data
gps_data = pd.DataFrame({"latitude": latitudes, "longitude": longitudes})
weather_data = pd.DataFrame(
    {"latitude": latitudes, "longitude": longitudes, "temperature": temperatures}
)

# Save to CSV files (optional, if you want to reuse the data)
gps_data.to_csv("gps_coordinates_italy.csv", index=False)
weather_data.to_csv("weather_data_italy.csv", index=False)
