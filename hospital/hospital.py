from data.data import emergency_hospitals_coord
from osrm_travel import get_time, to_osrm

SAHLGRENSKA = "Sahlgrenska Universitetssjukhuset"

def name_to_coord(name):
    if name not in emergency_hospitals_coord:
        raise ValueError(f"Hospital '{name}' not found.")
    return emergency_hospitals_coord[name]


def two_nearest_hospitals(origin, hospitals):
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
    times = [(hospital, get_time(to_osrm(origin), to_osrm(name_to_coord(hospital)))) for hospital in hospitals]

    # Sort by travel time
    times.sort(key=lambda x: x[1])

    time_to_sahl1 = times[0][1] + get_time(to_osrm(name_to_coord(times[0][0])), to_osrm(name_to_coord(SAHLGRENSKA)))
    time_to_sahl2 = times[1][1] + get_time(to_osrm(name_to_coord(times[1][0])), to_osrm(name_to_coord(SAHLGRENSKA)))

    if time_to_sahl2 < time_to_sahl1 and times[1][1] < 900:
        print(times[0])
    else:
        print(times[1])