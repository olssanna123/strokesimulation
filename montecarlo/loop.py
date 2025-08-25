from data.data import get_borders, get_hospitals
from hospital.hospital import name_to_coord, get_emergency_hospital
from origin.origin import draw_sample, get_origin


def loop(sampling_array):
    mun = draw_sample(sampling_array)
    borders = get_borders(mun)
    origin = get_origin(borders)
    hospitals = get_hospitals()
    emergency_hospital = get_emergency_hospital(origin, hospitals)

    res = {
        "Origin": origin,
        "Emergency hospital": emergency_hospital[0]
    }

    if emergency_hospital == "Sahlgrenska Universitetssjukhuset":
        print("Sahlgrenska Universitetssjukhuset is the closest emergency hospital!")
        saved_time = 0
        print("Saved time is " + str(saved_time) + " seconds")

    return res