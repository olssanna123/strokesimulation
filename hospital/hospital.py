# Hospital
from data.data import emergency_hospitals, emergency_hospitals_coord
from google_travel_calc import get_time


# Find the closest emergency hospital
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

# Convert name to coordinates of emergency hospital
def name_to_coord(name):
    return emergency_hospitals_coord[name]

# Decision rules

# Hospital in adjacent region