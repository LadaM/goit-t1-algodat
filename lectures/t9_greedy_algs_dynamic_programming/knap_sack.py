def knap_sack(max_weight, weights, values, n):
    """
    A recursive solution to the 0/1 Knapsack Problem.
    
    Parameters:
    - max_weight: the maximum weight the knapsack can hold
    - weights: a list of weights of the items
    - values: a list of values of the items
    - n: the number of items
    
    Returns:
    - The maximum value that can be obtained by selecting a subset of the items and fitting them into the knapsack without exceeding its weight limit.
    """

    # base case
    if n == 0 or max_weight == 0:
        return 0

    # if the weight of the nth item is more than the capacity of the knapsack, it cannot be included
    if weights[n - 1] > max_weight:
        return knap_sack(max_weight, weights, values, n - 1)

    # returning the maximum of two cases:
    # (1) n-th item inckuded
    # (2) not included
    else:
        return max(
            values[n - 1] + knap_sack(max_weight - weights[n - 1], weights, values, n - 1),
            knap_sack(max_weight, weights, values, n - 1),
        )

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight

def knap_sack_greedy(items: list[Item], capacity: int) -> int:
    """
    A function to solve the 0/1 knapsack problem using a greedy approach.
    
    Parameters:
    - items: a list of Item objects representing the items available for selection
    - capacity: an integer representing the maximum weight the knapsack can hold
    
    Returns: an integer representing the maximum value that can be obtained by always choosing the best weight to value ratio
    """
    items.sort(key=lambda x: x.ratio, reverse=True)
    total_value = 0
    for item in items:
        if capacity >= item.weight:
            capacity -= item.weight
            total_value += item.value
    return total_value


def knap_sack_dynamic(capacity, weights, values, n):
    """
    A function to solve the 0/1 knapsack problem using dynamic programming.
    
    Parameters:
    - capacity: integer representing the maximum capacity of the knapsack
    - weights: list of integers representing the weights of the items
    - values: list of integers representing the values of the items
    - n: integer representing the number of items
    
    Returns: integer representing the maximum value that can be put in a knapsack of capacity
    """
    # creating a table for storing solutions to subproblems
    solutions = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # building the table bottom-up
    # for item i
    for i in range(n + 1):
        # for each capacity
        for w in range(capacity + 1):
            # base cases
            if i == 0 or w == 0:
                solutions[i][w] = 0
            # item fits
            elif weights[i - 1] <= w:
                # choosing if current item is better to be included or not
                solutions[i][w] = max(values[i - 1] + solutions[i - 1][w - weights[i - 1]], 
                                      solutions[i - 1][w])
            # item doesn't fit -> previous value
            else:
                solutions[i][w] = solutions[i - 1][w]

    return solutions[n][capacity]


if __name__ == "__main__":
    # testing recursive solution
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50
    n = len(values)
    print("Recursive: ", knap_sack(capacity, weights, values, n))  # 220

    # testing greedy solution
    items = [Item(10, 60), Item(20, 100), Item(30, 120)]
    capacity = 50
    print("Greedy: ", knap_sack_greedy(items, capacity))  # 160

    # testing dynamic solution
    print("Dynamic: ", knap_sack_dynamic(capacity, weights, values, n))  # 220
