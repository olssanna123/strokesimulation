# Main
from data.data import create_sampling_array
from montecarlo.montecarlo import monte_carlo


def main():
    samp_arr = create_sampling_array()
    samp = monte_carlo(samp_arr)
    print(samp)
    return

main()