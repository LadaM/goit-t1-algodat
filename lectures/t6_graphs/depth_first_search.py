def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=' ')  # visit vertex
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)


def dfs_iterative(graph, start_vertex):
    visited = set()
    # using stack to store visited vertices
    stack = [start_vertex]  
    while stack:
        vertex = stack.pop()  
        if vertex not in visited:
            print(vertex, end=' ')  # visit vertex
            visited.add(vertex)
            stack.extend(reversed(graph[vertex]))  
    return visited


if __name__ == '__main__':
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    dfs_recursive(graph, 'A')
