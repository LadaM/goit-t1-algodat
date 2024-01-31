def linear_search(arr, elem):
    if arr is None or len(arr) == 0:
        return -1
    for i in range(len(arr)):
        if arr[i] == elem:
            return i
    return -1


def contains(arr, elem):
    return linear_search(arr, elem) > -1
