from collections import deque

def bfs_iterative(graph, start):
    visited = set()
    # initialization of the queue with the start vertex
    queue = deque([start])

    while queue:  # while the queue is not empty
        # getting the first on the queue (FIFO)
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=" ")  # visit vertex
            visited.add(vertex)
            # adding all unvisited neighbors to the queue
            queue.extend(set(graph[vertex]) - visited)

    return visited  


def bfs_recursive(graph, queue, visited=None):
    if visited is None:
        visited = set()
    if not queue:
        return
    # getting the first on the queue (FIFO)
    vertex = queue.popleft()
    if vertex not in visited:
        print(vertex, end=" ")  # visit vertex
        visited.add(vertex)
        # adding all unvisited neighbors to the queue
        queue.extend(set(graph[vertex]) - visited)
    # recursive call
    bfs_recursive(graph, queue, visited)


if __name__ == '__main__':
    graph = {
        'A': ['B', 'C', 'F'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    print("Iterative: ")
    bfs_iterative(graph, 'A')
    print("\nRecursive: ")
    bfs_recursive(graph, deque(["A"]))