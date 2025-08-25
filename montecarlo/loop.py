from data.data import get_borders, emergency_hospitals
from hospital.hospital import find_emergency_hospital, name_to_coord
from origin.origin import draw_sample, get_origin
from osrm_travel import get_time, to_osrm


def loop(sampling_array):
    mun = draw_sample(sampling_array)
    borders = get_borders(mun)
    origin = get_origin(borders)
    emergency_hospital = find_emergency_hospital(origin, emergency_hospitals)

    if emergency_hospital == "Sahlgrenska Universitetssjukhuset":
        print("Sahlgrenska Universitetssjukhuset is the closest emergency hospital!")
        saved_time = 0
        print("Saved time is " + str(saved_time) + " seconds")
#        write_saved(saved_time)
    else:
        print("Time from origin to emergency hospital is: ")
        time1 = emergency_hospital[1]
        print(str(time1) + " seconds")

        print("Time from emergency hospital to Sahlgrenska is: ")
        time2 = get_time(to_osrm(name_to_coord(emergency_hospital[0])), to_osrm(name_to_coord("Sahlgrenska Universitetssjukhuset")))
        print(str(time2) + " seconds")

        print("Time straight from origin to Sahlgrenska is: ")
        time3 = get_time(to_osrm(origin), to_osrm(name_to_coord("Sahlgrenska Universitetssjukhuset")))
        print(str(time3) + " seconds")

        #write_saved(saved_time)

    res = {
        "Origin": origin,
        "Emergency hospital": emergency_hospital[0],
    }

    return res