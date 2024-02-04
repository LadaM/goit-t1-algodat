def dijkstra(graph, start):
    # initialization of the distances that are at this point unknown
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0  # setting the distance from the start vertex to itself to 0
    unvisited = list(graph.keys())

    while unvisited:
        # finding the vertex with the minimum distance to it
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight

            # if new distance is smaller, update the distance
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        # delete the current vertex from the unvisited list
        unvisited.remove(current_vertex)

    return distances


if __name__ == '__main__':
    graph = {
        'A': {'B': 5, 'C': 10},
        'B': {'A': 5, 'D': 3},
        'C': {'A': 10, 'D': 2},
        'D': {'B': 3, 'C': 2, 'E': 4},
        'E': {'D': 4}
    }

    print(dijkstra(graph, 'A'))
