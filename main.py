# Main

from data.data import create_sampling_array, get_borders
from hospital.hospital import name_to_coord
from origin.origin import draw_sample, get_origin
from osrm_travel import get_time


def convert_seconds(seconds):
    if seconds is None or seconds < 0:
        return "00:00:00"
    units = [("hours", 3600), ("minutes", 60), ("seconds", 1)]
    values = []
    for _, value in units:
        count = seconds // value
        seconds -= count * value
        values.append(count)
    return f"{values[0]:02d}:{values[1]:02d}:{values[2]:02d}"

def main():
    array = create_sampling_array()
    mun = draw_sample(array)
    borders = get_borders(mun)
    origin = get_origin(borders)
    print(origin)
    origin_formatted = (origin[1],origin[0])
    print(origin_formatted)
    time = get_time(origin_formatted, name_to_coord("Sahlgrenska Universitetssjukhuset"))
    print(convert_seconds(time))
    return

main()
