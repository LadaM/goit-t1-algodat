from math import sqrt
from itertools import combinations


def held_karp(distance_matrix):
    n = len(distance_matrix)
    # initialize the table
    # using tuples to represent combinations of cities
    dp = {(frozenset([0, i]), i): (distance_matrix[0][i], [0, i])
          for i in range(1, n)}
    # base case
    dp[(frozenset([0]), 0)] = (0, [0])

    for r in range(2, n + 1):
        for subset in combinations(range(1, n), r):
            subset = frozenset(subset) | frozenset([0])
            for next_city in subset:
                if next_city == 0:
                    continue
                prev_subset = subset - frozenset([next_city])
                dp[(subset, next_city)] = min(
                    (
                        dp[(prev_subset, last_city)][0]
                        + distance_matrix[last_city][next_city],
                        dp[(prev_subset, last_city)][1] + [next_city],
                    )
                    for last_city in prev_subset
                    if last_city != 0
                )

    # finding the minimum distance path with return to the original city
    all_cities = frozenset(range(n))
    result = min(
        (
            dp[(all_cities, last_city)][0] + distance_matrix[last_city][0],
            dp[(all_cities, last_city)][1] + [0],
        )
        for last_city in range(1, n)
    )

    return result


def calculate_distance(coord1, coord2):
    return sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)


if __name__ == '__main__':

    # cities coordinates
    cities = {"A": (0, 0), "B": (1, 5), "C": (2, 2), "D": (3, 3), "E": (5, 1)}

    # create distance matrix
    distance_matrix = []
    for i, source in enumerate(cities.values()):
        distance_matrix.append([])
        for target in cities.values():
            distance_matrix[i].append(calculate_distance(source, target))

    result, path = held_karp(distance_matrix)
    print(result, path)
    # getting the names of the cities on the shortest path
    city_names = list(cities.keys())
    path_with_names = [city_names[i] for i in path]

    print(result, path_with_names)
