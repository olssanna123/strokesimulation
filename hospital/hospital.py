# Hospital

# Imports

# --------------------
# Get the calculated travel time between two destinations

def get_time(origin, destination):
    pass

# --------------------
# Get the time difference

def time_difference(a, b):
    if (a > b):
        return a-b
    else:
        return 0

# --------------------
# Get time at hospital in sec

def get_time_at_hospital():
    pass

# --------------------
# Get the travel time
# Calculate travel time to emergency hospital in sec
# Calculate travel time from emergency hospital to final hospital in sec
# Calculate total time from origin to final hospital via emergency hospital in sec
# Calculate time from origin to final hospital in sec

def get_travel_time(origin, emergency_hospital, final_hospital):

    # Calculate the travel time from origin to the emergency hospital
    origin_to_emergency_hospital = get_time(origin, emergency_hospital)

    # Time at the emergency hospital
    time_at_emergency_hospital = get_time_at_hospital()

    # Calculate the travel time from the emergency hospital to the final hospital
    emergency_hospital_to_final_hospital = get_time(emergency_hospital, final_hospital)

    # Total travel time from origin to final hospital via emergency hospital
    total_time_via_emergency_hospital = origin_to_emergency_hospital + time_at_emergency_hospital +  emergency_hospital_to_final_hospital

    # Calculate travel time from origin straight to final hospital
    origin_to_final_hospital = get_time(origin, final_hospital)

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

# List with the emergency hospital in VGR
emergency_hospitals = [("Kungälvs sjukhus", (57.878303, 11.969459)), ("Norra Älvsborgs länssjukhus", (58.318547, 12.265819)), ("Södra Älvsborgs Sjukhus", (57.724261, 12.961380)), ("Alingsås lasarett", (57.928649, 12.521170)), ("Skaraborgs Sjukhus Skövde", (58.426663, 13.851575)), ("Sahlgrenska Universitetssjukhuset", (57.6833, 11.9549))]
emergency_hospitals_coord = {
    "Kungälvs sjukhus": (57.878303, 11.969459),
    "Norra Älvsborgs länssjukhus": (58.318547, 12.265819),
    "Södra Älvsborgs Sjukhus": (57.724261, 12.961380),
    "Alingsås lasarett": (57.928649, 12.521170),
    "Skaraborgs Sjukhus Skövde": (58.426663, 13.851575),
    "Sahlgrenska Universitetssjukhuset": (57.6833, 11.9549)
}

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

# --------------------
# Decision rules

# --------------------
# Hospital in adjacent region

# --------------------

def name_to_coord(name):
    return emergency_hospitals_coord[name]

def test_name_to_coord():
    print(name_to_coord("Kungälvs sjukhus"))

