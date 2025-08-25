from data.data import emergency_hospitals_coord
from osrm_travel import get_time, to_osrm

SAHLGRENSKA = "Sahlgrenska Universitetssjukhuset"

def name_to_coord(name):
    if name not in emergency_hospitals_coord:
        raise ValueError(f"Hospital '{name}' not found.")
    return emergency_hospitals_coord[name]

def find_emergency_hospital(origin, emergency_hospitals):
    """
    Finds the two closest hospitals based on travel time and applies decision rules.
    Assumes travel time is in seconds.
    """
    if len(emergency_hospitals) < 2:
        raise ValueError("Need at least two hospitals.")

    # Precompute all coordinates
    coords_cache = {}
    def get_coord(name):
        if name not in coords_cache:
            coords_cache[name] = to_osrm(name_to_coord(name))
        return coords_cache[name]

    origin_coord = get_coord(origin)
    sahl_coord = get_coord(SAHLGRENSKA)

    travel_times = []

    for hospital in emergency_hospitals:
        try:
            hospital_coord = get_coord(hospital)
            travel_time = get_time(origin_coord, hospital_coord)
            travel_times.append((hospital, travel_time))
        except Exception as e:
            print(f"Error fetching time for {hospital}: {e}")

    if len(travel_times) < 2:
        raise ValueError("Not enough valid hospitals after computing travel times.")

    travel_times.sort(key=lambda x: x[1])

    closest, second_closest = travel_times[:2]
    difference = abs(second_closest[1] - closest[1])

    # Get Sahlgrenska distances
    closest_sahl = get_time(get_coord(closest[0]), sahl_coord)
    second_closest_sahl = get_time(get_coord(second_closest[0]), sahl_coord)

    if second_closest_sahl < closest_sahl and difference < 900:  # 15 min = 900 sec
        return second_closest
    return closest
