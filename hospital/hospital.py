from data.data import emergency_hospitals_coord
from osrm_travel import get_time, format_coordinates

SAHLGRENSKA = "Sahlgrenska Universitetssjukhuset"

def name_to_coord(name):
    if name not in emergency_hospitals_coord:
        raise ValueError(f"Hospital '{name}' not found.")
    return emergency_hospitals_coord[name]


def get_emergency_hospital(origin, hospitals):
    """
    Returns the two hospitals with the least travel time from origin.

    Parameters:
    - origin: starting point
    - hospitals: list of hospital locations

    Returns:
    - A list of two hospitals with the smallest travel time
    """
    if len(hospitals) < 2:
        return hospitals  # return whatever is available

    # Create a list of (hospital, travel_time) tuples
    times = [(hospital, get_time(origin, name_to_coord(hospital))) for hospital in hospitals]

    # Sort by travel time
    times.sort(key=lambda x: x[1])
    print(times)