def floyd_warshall(graph):
    # number of vertices
    n = len(graph)
    
    # initialize distance matrix
    distance = [[float('inf')] * n for _ in range(n)]
    
    # putting 0's on the diagonal (distance from the city to itself is 0)
    for i in range(n):
        distance[i][i] = 0
    
    # putting in the distance between the cities
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                distance[i][j] = graph[i][j]
    
    # updating the distance
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    
    return distance


if __name__ == "__main__":
    # adjacency matrix
    m = [
        [0, 3, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 7, 0, 2],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 3],
        [0, 0, 0, 0, 0, 0]
    ]

    distance_matrix = floyd_warshall(m)
    for row in distance_matrix:
        print(row)
