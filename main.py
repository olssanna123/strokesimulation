# Main
from data.data import create_sampling_array, get_borders
from hospital.hospital import name_to_coord
from origin.origin import draw_sample, get_origin
from osrm_travel import to_osrm, get_time


def main():
    array = create_sampling_array()
    mun = draw_sample(array)
    print("Municipality is: " + mun)
    borders = get_borders(mun)
    origin = get_origin(borders)
    print("Origin is: " + str(origin))
    time1 = get_time(to_osrm(origin), name_to_coord("Alingsås lasarett"))
    print(time1)
    return

main()
