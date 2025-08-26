# Main
from data.data import create_sampling_array
from montecarlo.loop import loop
from result.result import create_saved_table, create_saved_avg_table


def main():
    create_saved_table()
    create_saved_avg_table()
    return

main()
