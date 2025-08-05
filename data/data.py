# Data
import geopandas as gpd
import pandas as pd

# --------------------
# Shapefile to GeoJSON
def shapefile_to_geojson(filename, filename_result):
    gdf = gpd.read_file(filename)
    gdf.to_file(filename_result, driver="GeoJSON")

# --------------------
# Filter GeoJSON file by list of municipality
def filter_by_municipalities(mun, filename, column_name, filename_result):
    # Load the GeoJSON file
    gdf = gpd.read_file(filename)
    # Filter by municipality name
    filtered_gdf = gdf[gdf[column_name].isin(mun)]
    # Save filtered data as a new GeoJSON
    filtered_gdf.to_file(filename_result, driver="GeoJSON")

# --------------------
# List of emergency hospitals
emergency_hospitals = [("Kungälvs sjukhus", (57.878303, 11.969459)), ("Norra Älvsborgs länssjukhus", (58.318547, 12.265819)), ("Södra Älvsborgs Sjukhus", (57.724261, 12.961380)), ("Alingsås lasarett", (57.928649, 12.521170)), ("Skaraborgs Sjukhus Skövde", (58.426663, 13.851575)), ("Sahlgrenska Universitetssjukhuset", (57.6833, 11.9549))]
emergency_hospitals_coord = {
    "Kungälvs sjukhus": (57.878303, 11.969459),
    "Norra Älvsborgs länssjukhus": (58.318547, 12.265819),
    "Södra Älvsborgs Sjukhus": (57.724261, 12.961380),
    "Alingsås lasarett": (57.928649, 12.521170),
    "Skaraborgs Sjukhus Skövde": (58.426663, 13.851575),
    "Sahlgrenska Universitetssjukhuset": (57.6833, 11.9549)
}

# --------------------
# Population data
# The number of citizens in each municipality
data = {
  "Kommun": ['Ale','Alingsås','Bengtsfors','Bollebygd','Borås','Dals-Ed','Essunga','Falköping','Färgelanda','Grästorp','Gullspång','Göteborg','Götene','Herrljunga','Hjo','Härryda','Karlsborg','Kungälv','Lerum','Lidköping','Lilla Edet','Lysekil','Mariestad','Mark','Mellerud','Munkedal','Mölndal','Orust','Partille','Skara','Skövde','Sotenäs','Stenungsund','Strömstad','Svenljunga','Tanum','Tibro','Tidaholm','Tjörn','Tranemo','Trollhättan','Töreboda','Uddevalla','Ulricehamn','Vara','Vårgårda','Vänersborg','Åmål','Öckerö'],
  "Folkmangd": [32446,42382,9138,9733,114592,4606,5656,32991,6434,5563,5119,604616,13218,9441,9258,39875,7061,49785,43706,40539,14426,13969,24647,35287,9165,10502,70534,15333,40730,18654,57763,9052,27862,13476,10759,12865,11332,12839,16146,11883,59073,9141,57045,25087,16066,12384,40012,12006,12819]
}

def get_population_data():
  return data

# --------------------
# Create sampling array
# Function creates an array with the name of the municipality repeated the number of times as the number of it's citizens
def create_sampling_array():
    data = get_population_data()
    df = pd.DataFrame(data)
    sampling_array_list_of_lists = []
    sampling_array = []
    i = 0
    while i < 49:
        name_region = df.loc[i].at["Kommun"]
        nb_citizens = df.loc[i].at["Folkmangd"]
        item = [name_region]*nb_citizens
        sampling_array_list_of_lists.append(item)
        i += 1
    # Make it a single list
    j = 0
    k = 0
    while j < 49:
        k = 0
        while k < len(sampling_array_list_of_lists[j]):
            tmp = sampling_array_list_of_lists[j][k]
            sampling_array.append(tmp)
            k += 1
        j += 1
    return sampling_array
