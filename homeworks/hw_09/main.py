from timeit import default_timer as timer
from numpy import random

from coin_selection_greedy import choose_coins_greedy
from coin_selection_dynamic import choose_coins_dynamic, get_min_number_of_coins


def measure_solution_time(coin_selection_func, coins, amounts):
    start = timer()
    for amount in amounts:
        coin_selection_func(coins, amount)
    end = timer()
    return end - start


def get_time_str_in_ms(time):
    return f"{time * 1000: .5f}"


def main():
    coins = {1, 2, 5, 10, 20, 50}  # the available coin denominations
    amounts_counts = [10, 100, 1000, 10000]

    print(f"|{'Algorithm':<20} | {'# Amounts':<10} | {'Time (ms)':<15}|")
    for ac in amounts_counts:
        change_amounts = random.randint(1, 1000, ac)  # random amounts to test

        greedy_solution_time = measure_solution_time(
            choose_coins_greedy, coins, change_amounts)
        dynamic_solution_time = measure_solution_time(
            choose_coins_dynamic, coins, change_amounts)
        dynamic_simpler_problem_solution_time = measure_solution_time(
            get_min_number_of_coins, coins, change_amounts)

        print(f"|{'-'*20} | {'-'*10} | {'-'*15}|")
        print(
            f"|{'Greedy':<20} | {ac:<10} | {get_time_str_in_ms(greedy_solution_time):<15}|")
        print(
            f"|{'Dynamic': <20} | {ac:<10} | {get_time_str_in_ms(dynamic_solution_time):<15}|")
        print(f"|{'Simple Dynamic':<20} | {ac:<10} | {get_time_str_in_ms(dynamic_simpler_problem_solution_time):<15}|")


if __name__ == "__main__":
    main()
