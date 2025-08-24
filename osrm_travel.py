import requests

from hospital.hospital import name_to_coord

def to_osrm(coord):
    """
    Convert a coordinate from (latitude, longitude) to (longitude, latitude)
    for OSRM.

    Parameters:
        coord (tuple): (latitude, longitude)

    Returns:
        tuple: (longitude, latitude)
    """
    lat, lon = coord
    return (lon, lat)


def get_time(start, end):
    # OSRM public demo server URL
    url = f"http://router.project-osrm.org/route/v1/driving/{start[0]},{start[1]};{end[0]},{end[1]}"

    # Add optional parameters: overview=false makes it faster, steps=false removes turn-by-turn details
    params = {
        "overview": "false",
        "steps": "false"
    }

    # Make request
    response = requests.get(url, params=params)

    # Check for success
    if response.status_code == 200:
        data = response.json()
        route = data['routes'][0]
        duration_sec = route['duration']
        distance_m = route['distance']
        print(f"Travel time: {duration_sec:.0f} seconds")
        print(f"Distance: {distance_m/1000:.2f} km")
        return duration_sec
    else:
        print(f"Error: {response.status_code}")

