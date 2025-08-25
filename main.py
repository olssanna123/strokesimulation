# Main
from data.data import get_hospitals
from hospital.hospital import get_emergency_hospital


def main():
    varberg = '57.10557, 12.25078'
    hospitals = get_hospitals()
    get_emergency_hospital(varberg, hospitals)
    return

main()
