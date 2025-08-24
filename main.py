# Main
from hospital.hospital import name_to_coord
from osrm_travel import get_travel_time

def main():

    malm = (55.60587, 13.00073)
    akut = name_to_coord("Kungälvs sjukhus")
    sahl = (57.6833306, 11.95499618)
    res = get_travel_time(malm, akut, sahl)
    print(res)
    return

main()
