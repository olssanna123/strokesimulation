# Main

from data.data import create_sampling_array


def convert_seconds(seconds):
    if seconds is None or seconds < 0:
        return "00:00:00"
    units = [("hours", 3600), ("minutes", 60), ("seconds", 1)]
    values = []
    for _, value in units:
        count = int(seconds // value)  # Convert to integer
        seconds -= count * value
        values.append(count)
    return f"{values[0]:02d}:{values[1]:02d}:{values[2]:02d}"

def main():
    return

main()
