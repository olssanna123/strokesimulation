# Main
from data.data import shapefile_to_geojson, get_municipalities, filter_by_municipalities
from origin.origin import get_borders


def main():
    shapefile_to_geojson("Kartogram_SE.shp", "Kartogram_SE")
    mun = get_municipalities()
    filter_by_municipalities(mun, "Kartogram_SE", "KnNamn", "Kartogram_SE_filtered")
    borders = get_borders("Kartogram_SE_filtered", "Härryda")
    print(borders)
    return

main()