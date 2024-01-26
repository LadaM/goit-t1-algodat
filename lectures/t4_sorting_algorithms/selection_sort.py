def selection_sort(arr, asc=True):
    n = len(arr)
    for i in range(n):
        target_idx = i
        for j in range(i + 1, n):
            if asc and arr[j] < arr[target_idx]:
                target_idx = j
            elif not asc and arr[j] > arr[target_idx]:
                target_idx = j
        arr[i], arr[target_idx] = arr[target_idx], arr[i]
    return arr


if __name__ == "__main__":
    sorted_asc = [1, 2, 3, 4, 5, 0, 0, -8]
    print("Descending:", selection_sort(sorted_asc, asc=False))

    sorted_desc = [5, 4, 3, 2, 1, 5000, 250]
    print("Ascending:", selection_sort(sorted_desc))
