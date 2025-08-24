# Origin
import random

import numpy as np
from shapely.geometry import Point

from shapely.geometry import Polygon

def coords_to_polygon(coords):
    """
    Convert a list of coordinates into a Shapely Polygon object.

    Args:
        coords (list of tuple): [(x1, y1), (x2, y2), ...]

    Returns:
        shapely.geometry.Polygon: Polygon object
    """
    if len(coords) < 3:
        raise ValueError("At least three coordinates are needed to form a polygon.")

    # Close polygon if not closed already
    if coords[0] != coords[-1]:
        coords = coords + [coords[0]]

    return Polygon(coords)


# Generate a random point within polygon and return coordinates
def get_origin(borders):
    poly = coords_to_polygon(borders)
    min_x, min_y, max_x, max_y = poly.bounds
    while (True):
        point = Point([random.uniform(min_x, max_x), random.uniform(min_y, max_y)])
        if (point.within(poly)):
            break
        else:
            continue
    point_tuple = (point.x, point.y)
    return point_tuple

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