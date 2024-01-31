import heapq


def heap_sort(iterable, reverse=False):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    if reverse:
        return [heapq.heappop(h) for _ in range(len(h))][::-1]
    return [heapq.heappop(h) for _ in range(len(h))]


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    sorted_arr = heap_sort(arr)
    print("Sorted asc:", sorted_arr)

    sorted_arr = heap_sort(arr, reverse=True)
    print("Sorted desc:", sorted_arr)
