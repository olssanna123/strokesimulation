# Main
from osrm_travel import get_time
from result.result import create_saved_table, create_saved_avg_table


def main():
    got = (57.70716, 11.96679)
    malm = (55.60587, 13.00073)
    res = get_time(got, malm)
    print(res)
    return

main()
