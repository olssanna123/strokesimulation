# Origin
import json
import random
import numpy as np
from shapely.geometry import Point

def extract_borders(filename, mun):
    """
        Extracts the feature mun from a GeoJSON feature collection

        Parameters:
            filename (str): A GeoJSON file.
            mun (str): The name of the municipality.

        Returns:
            GeoJSON feature
            None

    """
    with open(filename, 'r', encoding='utf-8') as f:
        geojson_data = json.load(f)

    for feature in geojson_data.get("features", []):
        if feature.get("properties", {}).get("KnNamn") == mun:
            return feature
    return None

def parse_borders(feature):
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
        res = {
            "Geom type": geom_type,
            "Polygon": coordinates[0]  # Outer ring
        }
        return res
    elif geom_type == "MultiPolygon":
        res = {
            "Geom type": geom_type,
            "MultiPolygon": [polygon[0] for polygon in coordinates]  # Outer rings of each polygon
        }
        return res
    else:
        raise ValueError(f"Unsupported geometry type: {geom_type}")

def convert_borders(coords):
    """
    Converts a list of EPSG:3006 (SWEREF99 TM) coordinates to WGS84 (EPSG: 4326) coordinates.

    Parameters:
        list: A list of EPSG:3006 coordinates.

    Returns:
        list: A list of EPSG: 4326 coordinates.
    """
    from pyproj import Transformer

    # Define the transformer: from EPSG:3006 (SWEREF99 TM) to EPSG:4326 (WGS84)
    transformer = Transformer.from_crs("EPSG:3006", "EPSG:4326", always_xy=True)

    coords_wgs84 = [transformer.transform(x, y) for x, y in coords]

    # Print or use in OSRM (format: lon,lat)
    for lon, lat in coords_wgs84:
        print(f"{lon},{lat}")

# Generate a random point within polygon and return coordinates
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
