# Main
from data.data import shapefile_to_geojson, get_municipalities, filter_by_municipalities


def main():
    shapefile_to_geojson("Kartogram_SE.shp", "Kartogram_SE")
    mun = get_municipalities()
    filter_by_municipalities(mun, "Kartogram_SE", "KnNamn", "Kartogram_SE_filtered")

    return

main()