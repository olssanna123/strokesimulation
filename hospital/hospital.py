# Hospital
from data.data import emergency_hospitals, emergency_hospitals_coord

# --------------------
# Helper functions
def get_time(origin, destination):  # Get the calculated travel time between two destinations
    pass

def time_difference(a, b):  # Get the time difference
    if (a > b):
        return a-b
    else:
        return 0

# --------------------
# Get time at hospital in sec
def get_time_at_hospital():
    pass

# --------------------
# Get travel time
def get_travel_time(origin, emergency_hospital, final_hospital):

    # Calculate the travel time from origin to the emergency hospital in sec
    origin_to_emergency_hospital = get_time(origin, emergency_hospital)

    # Time at the emergency hospital in sec
    time_at_emergency_hospital = get_time_at_hospital()

    # Calculate the travel time from the emergency hospital to the final hospital in sec
    emergency_hospital_to_final_hospital = get_time(emergency_hospital, final_hospital)

    # Total travel time from origin to final hospital via emergency hospital in sec
    total_time_via_emergency_hospital = origin_to_emergency_hospital + time_at_emergency_hospital +  emergency_hospital_to_final_hospital

    # Calculate travel time from origin straight to final hospital in sec
    origin_to_final_hospital = get_time(origin, final_hospital)

    # Calculate the saved time going straight to final hospital
    saved_time = time_difference(total_time_via_emergency_hospital, origin_to_final_hospital)

    travel_time = {
        "origin to emergency hospital": origin_to_emergency_hospital,
        "time at emergency hospital": time_at_emergency_hospital,
        "emergency hospital to final hospital": emergency_hospital_to_final_hospital,
        "total time via emergency hospital": total_time_via_emergency_hospital,
        "origin to final hospital": origin_to_final_hospital,
        "saved time": saved_time
    }

    return travel_time

# --------------------
# Find closest emergency hospital

def get_emergency_hospital(origin):
    closest_emergency_hospital = emergency_hospitals[0][0]
    min_time = get_time(origin, emergency_hospitals[0][1])
    i = 1
    while i < len(emergency_hospitals):
        tmp = get_time(origin, emergency_hospitals[i][1])
        if tmp < min_time:
            closest_emergency_hospital = emergency_hospitals[i][0]
            min_time = tmp
        i = i + 1
    return closest_emergency_hospital

def name_to_coord(name):
    return emergency_hospitals_coord[name]

# --------------------
# Decision rules

# --------------------
# Hospital in adjacent region
