def binary_fraction_search(arr, key):
    """
    Perform a binary search on the given array of floats to find the specified key or the next closest key.
    Args:
        arr (list): The input list containing floating numbers sorted in ascending order to be searched.
        key: The value to be searched for in the list.
    Returns:
        int: The number of iterations it took to find the key.
        int: The index of the key or the next closest key in the array if found, otherwise -1
    """
    iterations = 0

    if arr is None or key is None or len(arr) < 1 or key > arr[-1]:
        return 0, -1

    if key <= arr[0]:
        return iterations, 0

    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right) // 2
        iterations += 1
        if arr[mid] == key:
            return iterations, mid
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid
    return iterations, right


if __name__ == "__main__":
    test_values = [0.1, 0.2, 0.3, 0.4, 0.45, 0.5, 0.6, 0.7, 0.8, 0.888, 0.9, 1, 1.05, 2.75]
    keys = [1, 0.3, 0.42, 0.89, 1.1, 2.5, -1, 0.65, 0.6, 3]

    for k in keys:
        print(f"{k: <5} --> {binary_fraction_search(test_values, k)}")
