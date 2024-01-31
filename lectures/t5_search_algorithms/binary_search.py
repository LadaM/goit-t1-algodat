import numpy as np


def binary_search(arr, elem):
    if arr is None or len(arr) == 0:
        return -1
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == elem:
            return mid
        elif arr[mid] < elem:
            low = mid + 1  # search right of mid
        else:
            high = mid - 1  # search left of mid
    return -1


if __name__ == "__main__":
    test_array = np.random.randint(0, 100, 100)
    search_for = 77
    while search_for not in test_array:
        search_for = np.random.randint(0, 100)
    print(f"Array: {test_array}")
    print(f"Searching for: {search_for}")
    print(f"Found at index: {binary_search(sorted(test_array), search_for)}")
