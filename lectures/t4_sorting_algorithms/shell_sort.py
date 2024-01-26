def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

    return arr


def shell_sort_info(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        print(f"GAP: =============={gap}===================")
        for i in range(gap, n):
            temp = arr[i]
            j = i
            print(f"i: ----------------- {i} ----------------")
            print(f"At the beginning of the loop {i}: {arr}")
            print(f"j: {j}, temp: {temp}, gap: {gap}")
            print(f"Comparing elements: {arr[j - gap]} > {temp}")
            while j >= gap and arr[j - gap] > temp:
                print(
                    f"Exchanged {arr[j - gap]} and {arr[j]}"
                )
                arr[j] = arr[j - gap]
                print(f"Array changed after j: {j}: {arr}")
                j -= gap
                print(f"j moved left: {j}")
            print(f"At the end of the for loop: {temp} put in place of {arr[j]}")
            arr[j] = temp
            print(f"After iteration {i}: {arr}")
        gap //= 2
        if gap == 0:
            print("Sorted")
    return arr


if __name__ == "__main__":
    arr = [5, 3, 999, 8, 6, 7, 2, 1000]
    print(shell_sort_info(arr))