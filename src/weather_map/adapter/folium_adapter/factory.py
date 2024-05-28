from weather_map.domain.model.border import Border


def border_to_geojson(*, border: Border) -> dict:
    """Convert a Border object to a GeoJSON dictionary.

    Parameters
    ----------
    border : Border
        The border object to be converted to GeoJSON format.

    Returns
    -------
    dict
        A dictionary representing the border in GeoJSON format.

    """
    return {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "MultiPolygon",
                    "coordinates": [
                        [
                            [
                                [coordinate.longitude, coordinate.latitude]
                                for coordinate in polygon.coordinates
                            ]
                            for polygon in border.polygons
                        ],
                    ],
                },
                "properties": {"name": "Border"},
            },
        ],
    }
