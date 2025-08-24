# Hospital
from data.data import emergency_hospitals_coord

# Convert name to coordinates of emergency hospital
def name_to_coord(name):
    return emergency_hospitals_coord[name]

# Decision rules

# Hospital in adjacent region