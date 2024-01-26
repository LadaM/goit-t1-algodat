import operator
import numpy as np


def merge_sort(a, asc=True):
    if len(a) <= 1:
        return a

    mid = len(a) // 2
    left_half = a[:mid]
    right_half = a[mid:]

    return merge(merge_sort(left_half, asc), merge_sort(right_half, asc), asc)


def merge(left, right, asc=True):
    merged = []
    left_index = 0
    right_index = 0

    # merge left and right
    comparator = operator.le if asc else operator.ge
    while left_index < len(left) and right_index < len(right):
        if comparator(left[left_index], right[right_index]):
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    # append remaining elements
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


if __name__ == "__main__":
    array = np.random.randint(0, 100, 10)
    print("Asc: ", merge_sort(array))
    print("Desc: ", merge_sort(array, False))
