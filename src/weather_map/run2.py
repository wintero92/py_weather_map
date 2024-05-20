from geopy.geocoders import Nominatim
from geopy.location import Location

def get_location(name):
    # Initialize the Nominatim geocoder
    geolocator = Nominatim(user_agent="geoapiExercises")
    
    # Get the location
    location: Location = geolocator.geocode(name)
    
    # Return the location details
    if location:
        return {
            "address": location.address,
            "latitude": location.latitude,
            "longitude": location.longitude
        }
    else:
        return None

# Example usage
place_name = "Sicily"
location = get_location(place_name)

if location:
    print(f"Address: {location['address']}")
    print(f"Latitude: {location['latitude']}")
    print(f"Longitude: {location['longitude']}")
else:
    print("Location not found.")
