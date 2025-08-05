# Main
from data.data import shapefile_to_geojson, get_municipalities, filter_by_municipalities
from origin.origin import get_borders


import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
import matplotlib.patches as patches

def plot_shapely_polygon(shapely_polygon):
    """
    Plots a Shapely Polygon on a 2D graph.

    Args:
        shapely_polygon (shapely.geometry.Polygon): A Shapely Polygon object.
    """
    if not isinstance(shapely_polygon, Polygon):
        raise TypeError("Input must be a shapely.geometry.Polygon")

    fig, ax = plt.subplots()

    # Exterior
    exterior_coords = list(shapely_polygon.exterior.coords)
    exterior_patch = patches.Polygon(exterior_coords, closed=True, edgecolor='black', facecolor='lightblue')
    ax.add_patch(exterior_patch)

    # Interiors (holes)
    for interior in shapely_polygon.interiors:
        interior_coords = list(interior.coords)
        hole_patch = patches.Polygon(interior_coords, closed=True, edgecolor='black', facecolor='white')
        ax.add_patch(hole_patch)

    # Set plot limits
    x_vals, y_vals = zip(*shapely_polygon.exterior.coords)
    ax.set_xlim(min(x_vals) - 1, max(x_vals) + 1)
    ax.set_ylim(min(y_vals) - 1, max(y_vals) + 1)
    ax.set_aspect('equal')
    ax.grid(True)
    plt.title("Shapely Polygon Plot")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.show()


def main():
    shapefile_to_geojson("Kartogram_SE.shp", "Kartogram_SE")
    mun = get_municipalities()
    filter_by_municipalities(mun, "Kartogram_SE", "KnNamn", "Kartogram_SE_filtered")
    borders = get_borders("Kartogram_SE_filtered", "Härryda")
    print(borders)
    plot_shapely_polygon(borders)
    return

main()