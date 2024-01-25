from copy import copy
from timeit import default_timer

import numpy as np

from insertion_sort import insertion_sort
from mergesort import merge_sort
from quicksort import quicksort

ARRAY_SIZE = 100000


def is_sorted(arr, reversed=False):
    return (
        all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
        if not reversed
        else all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1))
    )


def measure_sorting_time(sorting_func, arr):
    if is_sorted(arr):
        print("Array is already sorted!")
        return None
    start = default_timer()
    sorting_func(arr)
    end = default_timer()
    return end - start


def format_sorting_times(algorithm_times):
    table_separator = "|" +"-" * 20 + "|" + "-" * 20 + "|"
    print(table_separator)
    print(f"{'|Sorting Algorithm':<20} |{'Time':<20}|")
    print(table_separator)
    for algorithm, time in algorithm_times.items():
        print(f"|{algorithm:<20}|{time:<20}|")
    print(table_separator)


def main():
    np.random.seed(42)
    print(f"Size of array: {ARRAY_SIZE}")
    # uniform distribution
    array = np.random.randint(0, 1000000, ARRAY_SIZE)
    print("\nChecking time for uniform distribution...")
    uniform_dist_sorting_times = {
        "Insertion sort": measure_sorting_time(insertion_sort, copy(array)),
        "Mergesort": measure_sorting_time(merge_sort, array),
        "Quicksort": measure_sorting_time(quicksort, array),
        "Timsort": measure_sorting_time(sorted, array),
    }
    format_sorting_times(uniform_dist_sorting_times)

    # normally distributed data
    array_norm = np.random.normal(0, 1, ARRAY_SIZE)
    print("\nChecking time for normally distributed data...")
    norm_dist_sorting_times = {
        "Insertion sort": measure_sorting_time(insertion_sort, copy(array_norm)),
        "Mergesort": measure_sorting_time(merge_sort, array_norm),
        "Quicksort": measure_sorting_time(quicksort, array_norm),
        "Timsort": measure_sorting_time(sorted, array_norm),
    }
    format_sorting_times(norm_dist_sorting_times)


if __name__ == "__main__":
    main()
