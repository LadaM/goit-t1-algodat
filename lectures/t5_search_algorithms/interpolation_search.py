def interpolation_search(arr, key):
    """
    Interpolation search works similarly to binary search, but better for large uniformly distributed data sets.
    If data is not uniformly distributed, then binary search is better.
    :param arr: ordered iterable
    :param key: int
    :return: int - index of the key or -1 if the key wasn't found
    """
    if arr is None or len(arr) == 0:
        return -1
    low = 0
    high = len(arr) - 1

    while low <= high and key >= arr[low] and key <= arr[high]:
        index = low + int(((float(high - low) / (arr[high] - arr[low])) * (key - arr[low])))
        if arr[index] == key:
            return index
        if arr[index] < key:
            low = index + 1
        else:
            high = index - 1

    return -1


if __name__ == "__main__":
    arr = [-1, 0, 2, 3, 4, 10, 40, 50]
    x = 10
    print(interpolation_search(arr, x))