from math import sqrt

import numpy as np

from linear_search import linear_search


def create_index(arr, step):
    index = []
    for i in range(0, len(arr), step):
        index.append((arr[i], i))  # (value, index) sorted
    return index


def search(arr, elem):
    if arr is None or len(arr) == 0 or elem < arr[0] or elem > arr[-1]:
        return -1

    if len(arr) < 10:
        return linear_search(arr, elem)

    # Build index
    index = create_index(arr, step=int(sqrt(len(arr))))

    # Binary search in the index to find the relevant range
    start, end = 0, len(index) - 1
    while start < end:
        mid = (start + end) // 2
        if index[mid][0] == elem:
            return index[mid][1]
        elif index[mid][0] < elem:
            start = mid + 1
        else:
            end = mid

    # Linear search in the identified range
    start_index = index[start - 1][1] if start > 0 else 0
    end_index = index[start][1] if start < len(index) else len(arr) - 1

    return linear_search(arr[start_index : end_index + 1], elem) + start_index


if __name__ == "__main__":
    hundred = np.arange(1, 100)
    test_data = [3, 10, 1, -10, 99, 0]
    for x in test_data:
        index_x = search(hundred, x)
        print(f"Found {x} at index {index_x}. Retrieved from array: {hundred[index_x]}")
