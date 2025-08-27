from data.data import get_borders, get_hospitals
from hospital.hospital import name_to_coord, get_emergency_hospital
from main import convert_seconds
from origin.origin import draw_sample, get_origin
from osrm_travel import get_time
from result.result import write_saved


def loop(sampling_array):
    mun = draw_sample(sampling_array)
    borders = get_borders(mun)
    origin = get_origin(borders)

    hospitals = get_hospitals()
    emergency_hospital = get_emergency_hospital(origin, hospitals)

    # Origin
    print(origin)
    origin_formatted = (origin[1],origin[0])
    print(origin_formatted)
    time = get_time(origin_formatted, name_to_coord("Sahlgrenska Universitetssjukhuset"))
    print(convert_seconds(time))



    res = {
        "Origin": origin,
        "Emergency hospital": emergency_hospital[0]
    }

    if emergency_hospital == "Sahlgrenska Universitetssjukhuset":
        print("Sahlgrenska Universitetssjukhuset is the closest emergency hospital!")
        saved_time = 0
        print("Saved time is " + str(saved_time) + " seconds")
        #write_saved(saved_time)
    else:
        print("The closest emergency hospital is " + emergency_hospital[0])
        via_emergency_hospital = get_time(origin, )

    return res