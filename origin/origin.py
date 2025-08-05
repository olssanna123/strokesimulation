# Origin
import json
import random
import numpy as np
from shapely.geometry import Point
from shapely.geometry import shape, Polygon, MultiPolygon
from pyproj import Transformer

# --------------------
# Randomly generated municipality
# Pseudo-random number generator. Seed used for reproducibility.
rng = np.random.default_rng(seed=12345)

# Return random integer between 0 and highest_number
def model(highest_number):
    return rng.integers(0, highest_number)

# Draw a sample from sampling_array between 0 and highest_number
def draw_sample(sampling_array):
    index = model(len(sampling_array))
    sample = sampling_array[index]
    return sample

# --------------------
# Helper functions
# Get GeoJSON municipality feature
def get_geojson_municipality_feature(geojson_filename, municipality):
    """
    Returns the feature from a GeoJSON file where properties['KnNamn'] matches the given municipality name.

    Args:
        municipality (str): The municipality name to look for.
        geojson_filename (str): The path to the GeoJSON file.

    Returns:
        dict or None: The matching feature, or None if not found.
    """
    with open(geojson_filename, 'r', encoding='utf-8') as f:
        geojson_data = json.load(f)

    for feature in geojson_data.get("features", []):
        if feature.get("properties", {}).get("KnNamn") == municipality:
            return feature
    return None

# GeoJSON to polygon

def parse_geojson_polygon_borders(feature):
    """
    Extracts only the border (outer ring) coordinates from a GeoJSON Polygon or MultiPolygon feature.

    Parameters:
        feature (dict): A GeoJSON Feature with Polygon or MultiPolygon geometry.

    Returns:
        list: A list of border coordinates.
              - For Polygon: a single list of coordinates (outer ring).
              - For MultiPolygon: a list of outer rings.

    Raises:
        ValueError: If the geometry type is unsupported.
    """
    if not isinstance(feature, dict):
        raise ValueError("Input must be a dictionary (GeoJSON Feature).")

    geometry = feature.get("geometry")
    if geometry is None:
        raise ValueError("Feature does not contain 'geometry'.")

    geom_type = geometry.get("type")
    coordinates = geometry.get("coordinates")

    if geom_type == "Polygon":
        return coordinates[0]  # Outer ring
    elif geom_type == "MultiPolygon":
        return [polygon[0] for polygon in coordinates]  # Outer rings of each polygon
    else:
        raise ValueError(f"Unsupported geometry type: {geom_type}")

# --------------------
# Get borders
def get_borders(filename, mun):
    feature = get_geojson_municipality_feature(filename, mun)
    if feature is None:
        print("The feature for " + mun + " not found in GeoJSON file.")
        raise ValueError(f"Municipality '{mun}' not found in GeoJSON file.")
    else:
        print("The feature collected from the geojson file is " + str(feature))
    pol = parse_geojson_polygon_borders(feature)
    return pol

# --------------------
# Generate random point within polygon and return coordinates
def get_origin(poly):
    min_x, min_y, max_x, max_y = poly.bounds
    while (True):
        point = Point([random.uniform(min_x, max_x), random.uniform(min_y, max_y)])
        if (point.within(poly)):
            break
        else:
            continue
    point_tuple = (point.x, point.y)
    return point_tuple

