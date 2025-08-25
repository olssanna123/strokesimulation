# Hospital
from data.data import emergency_hospitals_coord, emergency_hospitals
from osrm_travel import get_time, to_osrm


# Convert name to coordinates of emergency hospital
def name_to_coord(name):
    return emergency_hospitals_coord[name]

# Decision rules
def find_two_closest_hospitals(origin):
    """
    Finds the two closest hospitals based on travel time and the difference between them.
    If the next closest hospital has less travel time to Sahlgrenska and the time difference between the travel time
    from origin to the emergency hospitals is less than 15 min (900 sec), the second closest hospital is returned.

    Parameters:
        origin (str): Starting location.
        emergency_hospitals (list): List of hospital names.
        get_time (function): A function that takes (start, end) and returns travel time in minutes.

    Returns:
        tuple: (hospital_name, travel_time)

    """
    if len(emergency_hospitals) < 2:
        raise ValueError("Need at least two hospitals to find two closest.")

    travel_times = []

    for hospital in emergency_hospitals:
        try:
            travel_time = get_time(origin, hospital)
            travel_times.append((hospital, travel_time))
        except Exception as e:
            print(f"Error fetching time for {hospital}: {e}")

    # Sort by travel time
    travel_times.sort(key=lambda x: x[1])

    closest = travel_times[0]
    second_closest = travel_times[1]
    difference = abs(second_closest[1] - closest[1])


    closest_sahl = get_time(to_osrm(name_to_coord(closest[0])), to_osrm(name_to_coord("Sahlgrenska Universitetssjukhuset")))
    second_closest_sahl = get_time(to_osrm(name_to_coord(second_closest[0])), to_osrm(name_to_coord("Sahlgrenska Universitetssjukhuset")))

    if second_closest_sahl < closest_sahl & difference < 900:
        return second_closest
    else:
        return closest
