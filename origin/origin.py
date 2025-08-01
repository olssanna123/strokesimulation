# Origin

# Imports
import geopandas as gpd
import json
import random
from shapely.geometry import Point
from shapely.geometry import Polygon
from shapely.geometry import shape, Polygon, MultiPolygon
import numpy as np


# RT90 (swedish grid) coordinates to ?

# --------------------
# Randomly generated municipality

# Pseudo-random number generator
# Seed used for reproducibility
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

# --------------------
# GeoJSON to polygon

def geojson_to_polygon(geojson):
    """
    Parses a GeoJSON feature and returns a Shapely Polygon.
    Accepts both Polygon and MultiPolygon geometry types.

    Args:
        geojson (dict): A GeoJSON-like dictionary containing a geometry.

    Returns:
        shapely.geometry.Polygon: A polygon representing the main area.
    """
    geom = shape(geojson['geometry'])

    if isinstance(geom, Polygon):
        polygon = geom
    elif isinstance(geom, MultiPolygon):
        # Pick the largest polygon by area
        polygon = max(geom.geoms, key=lambda p: p.area)
    else:
        print("GeoJSON geometry must be of type 'Polygon' or 'MultiPolygon'.")
        raise ValueError("Unsupported geometry type: " + str(geojson['geometry']['type']))

    if not polygon.is_valid:
        print("Invalid polygon geometry.")
        raise ValueError("Invalid polygon geometry.")

    return polygon

# --------------------
# Get borders GeoJSON

def get_borders_geojson(geojson_filename, municipality):
    feature = get_geojson_municipality_feature(geojson_filename, municipality)
    if feature is None:
        print("The feature for " + municipality + " not found in GeoJSON file.")
        raise ValueError(f"Municipality '{municipality}' not found in GeoJSON file.")
    else:
        print("The feature collected from the geojson file is " + str(feature))
    pol = geojson_to_polygon(feature)
    return pol

# --------------------
# Generate random point within polygon and return coordinates

def get_random_point(poly):
    min_x, min_y, max_x, max_y = poly.bounds
    while (True):
        point = Point([random.uniform(min_x, max_x), random.uniform(min_y, max_y)])
        if (point.within(poly)):
            break
        else:
            continue
    point_tuple = (point.x, point.y)
    return point_tuple