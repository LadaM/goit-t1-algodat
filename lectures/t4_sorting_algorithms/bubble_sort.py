def bubble_sort(arr, acs=True):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1): 
            if acs and arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            elif not acs and arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == '__main__':
    arr = [5, 3, 8, 6, 7, 2, 1000]
    print(bubble_sort(arr))
