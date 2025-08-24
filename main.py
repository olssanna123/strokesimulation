# Main
from data.data import create_sampling_array, get_borders
from origin.origin import draw_sample, get_origin


def main():
    array = create_sampling_array()
    mun = draw_sample(array)
    borders = get_borders(mun)
    origin = get_origin(borders)
    print(origin)
    return

main()
