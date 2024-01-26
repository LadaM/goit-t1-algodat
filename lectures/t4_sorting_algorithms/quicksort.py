def quicksort(arr, descending=False):
    """
    Sorts the input array using the quicksort algorithm.
    Args:
        arr: The array to be sorted.
        descending: A boolean indicating whether to sort in reversed order (default is False).
    Returns:
        The sorted array, by default in ascending order.
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    lower = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    higher = [x for x in arr if x > pivot]
    return (quicksort(higher, descending=descending) + middle + quicksort(lower, descending=descending)
            if descending
            else quicksort(lower, descending=descending) + middle + quicksort(higher, descending=descending))


if __name__ == "__main__":
    test_array = [5, 3, 8, 6, 7, 2, 1000]
    print("Asc: ", quicksort(test_array))
    print("Desc: ", quicksort(test_array, descending=True))
