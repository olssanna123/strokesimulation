# Main
from data.data import create_sampling_array
from montecarlo.loop import loop


def main():
    array = create_sampling_array()
    res = loop(array)
    print(res)
    return

main()
