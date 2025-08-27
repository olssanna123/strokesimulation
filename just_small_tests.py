from data.data import create_sampling_array, get_borders
from hospital.hospital import name_to_coord
from main import convert_seconds
from origin.origin import draw_sample, get_origin
from osrm_travel import get_time

x = create_sampling_array()

i = 0
while i < 30:
    mun = draw_sample(x)
    print(mun)
    borders = get_borders(mun)
    origin = get_origin(borders)
    print(origin)
    origin_formatted = (origin[1], origin[0])
    print(origin_formatted)
    time = get_time(origin_formatted, name_to_coord("Sahlgrenska Universitetssjukhuset"))
    print(convert_seconds(time))
    i += 1

