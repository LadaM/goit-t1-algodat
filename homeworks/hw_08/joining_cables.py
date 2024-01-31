import heapq


def get_cost_for_connecting_cables_heap(cables):
    """
    There are several network cables of different lengths, and you need to connect them two at a time into one cable
    using connectors in the order that will result in the lowest cost.
    The cost of connecting two cables is equal to the sum of their lengths,
    so the total cost is equal to the sum of the cables connected.
    """

    heapq.heapify(cables)  # build a min-heap

    total_cost = 0

    while len(cables) > 1:
        # Extract the two shortest cables from the heap
        cable1 = heapq.heappop(cables)
        cable2 = heapq.heappop(cables)

        connected_cable = cable1 + cable2
        total_cost += connected_cable
        print(f"Connected cable {cable1} and {cable2} into {connected_cable}.")

        # Add the connected cable back to the heap
        heapq.heappush(cables, connected_cable)

    return cables.pop(), total_cost  # return the connected cable and the total cost


def get_cost_connecting_cables_sorting(cables):
    if cables is None or len(cables) == 0:
        return None, 0
    
    if len(cables) == 1:
        return cables[0], 0

    sorted_cables = sorted(cables)
    cost = 0
    connected_cable = sorted_cables.pop(0)
    while len(sorted_cables) > 0:
        connected_cable += sorted_cables.pop(0)
        cost += connected_cable
    
    return connected_cable, cost


if __name__ == "__main__":
    cables = [1, 2, 3, 4, 5, 6]
    
    heap_res = get_cost_for_connecting_cables_heap(cables)
    print(f"Total cost of joining the cables = {heap_res}.")

    cables = [6, 2, 5, 1, 3, 4]
    print("Alternative solution (without using heap):")
    alternative_res = get_cost_connecting_cables_sorting(cables)
    print(f"Total cost of joining the cables = {alternative_res}.")
