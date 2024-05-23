import folium
import osmnx as ox

# Get the border data for Italy
gdf = ox.geometries_from_place("Sicily", {"boundary": "administrative"})

# Extract the polygon of Italy's border (admin_level 2 is the country level)
italy_border = gdf[gdf["admin_level"] == "2"].geometry.unary_union

# Initialize the map centered around Italy
map_center = [41.8719, 12.5674]  # Center of Italy
mymap = folium.Map(location=map_center, zoom_start=6, tiles="OpenStreetMap")


# Function to convert shapely geometry to GeoJSON format
def shapely_to_geojson(geometry):
    if geometry.type == "Polygon":
        return {
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": [list(geometry.exterior.coords)],
            },
            "properties": {},
        }
    elif geometry.type == "MultiPolygon":
        return {
            "type": "Feature",
            "geometry": {
                "type": "MultiPolygon",
                "coordinates": [[list(poly.exterior.coords)] for poly in geometry],
            },
            "properties": {},
        }


# Convert the Italy border to GeoJSON
italy_geojson = shapely_to_geojson(italy_border)

# Add the Italy border to the map
folium.GeoJson(
    italy_geojson,
    style_function=lambda x: {"color": "blue", "weight": 2, "fillOpacity": 0.1},
).add_to(mymap)

# Save the map to an HTML file
mymap.save("italy_border_map.html")
