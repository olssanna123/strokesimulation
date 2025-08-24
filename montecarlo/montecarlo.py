from data.data import get_borders
from hospital.hospital import get_emergency_hospital
from origin.origin import draw_sample, get_origin
from osrm_travel import get_travel_time
from result.result import write_saved


def loop_demo(sampling_array, final_hospital):
    mun = draw_sample(sampling_array)
    borders = get_borders(mun)
    origin = get_origin(borders)
    emergency_hospital = get_emergency_hospital(origin)

    time = get_travel_time(origin, emergency_hospital, final_hospital)

    if emergency_hospital == "Sahlgrenska Universitetssjukhuset":
        print("Sahlgrenska Universitetssjukhuset")
        saved_time = 0
        write_saved(saved_time)
    else:
        saved_time = time["Origin to emergency hospital"]["total"]  + 7200 + time["Emergency hospital to final hospital"]["total"] - time["Origin to final hospital"]["total"]
        print("Saved time")
        print(saved_time)
        write_saved(saved_time)

    res = {
        "Origin": origin,
        "Emergency hospital": emergency_hospital,
    }

    return res