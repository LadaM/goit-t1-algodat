import operator

import numpy as np


def insertion_sort(arr, asc=True):
    for i in range(1, len(arr)):
        key = arr[i]  # denotes the border of the sorted portion of the array
        j = i - 1
        compare = operator.le if asc else operator.ge
        while j >= 0 and compare(key, arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == "__main__":
    array = np.random.randint(0, 100, 10)
    print("Asc: ", insertion_sort(array))
    print("Desc: ", insertion_sort(array, False))
