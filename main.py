# Main
import matplotlib.pyplot as plt

from origin.origin import extract_borders, parse_borders


def plot_points(points):
    # Separate the input into x and y lists
    x_vals = [point[0] for point in points]
    y_vals = [point[1] for point in points]

    # Plot the points
    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_vals, marker='o', linestyle='-')

    # Optionally, connect the last point to the first to close the shape
    plt.plot([x_vals[-1], x_vals[0]], [y_vals[-1], y_vals[0]], marker='o', linestyle='-')

    plt.title('Plot of Points')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()

def main():
    borders = extract_borders("Kartogram_SE_filtered", "Härryda")
    print(borders)
    parsed_borders = parse_borders(borders)
    print(parsed_borders)
    plot_points(parsed_borders["Polygon"])

    return

main()