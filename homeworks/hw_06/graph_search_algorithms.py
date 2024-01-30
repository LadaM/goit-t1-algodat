import matplotlib.pyplot as plt
import networkx as nx


def bfs(graph, start_node):
    visited = set()
    visit_order = []
    queue = [start_node]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            print("." * len(visited), node)
            visited.add(node)
            visit_order.append(node)
            queue.extend([n for n in graph.neighbors(node) if n not in visited])

    return visit_order


def dfs(graph, start_node):
    visited = set()
    visit_order = []
    stack = [start_node]
    while stack:
        node = stack.pop()
        if node not in visited:
            print("." * len(visited), node)
            visited.add(node)
            visit_order.append(node)
            stack.extend([n for n in graph.neighbors(node) if n not in visited])

    return visit_order


if __name__ == "__main__":
    G = nx.Graph()
    G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6)])
    print("BFS:")
    bfs(G, 1)
    print("DFS:")
    dfs(G, 1)
    nx.draw(G, with_labels=True, node_color="lightblue", edge_color="gray")
    # plt.show()
