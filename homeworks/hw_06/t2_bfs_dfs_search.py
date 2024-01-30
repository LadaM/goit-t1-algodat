import matplotlib.pyplot as plt
import networkx as nx

from graph_search_algorithms import bfs, dfs
from t1_network_modelling import (
    create_lines_network_graph,
    get_sbb_route_network_data,
)


def main():
    # Get the graph from the file t1_network_modelling.py
    lines_data = get_sbb_route_network_data()
    graph = create_lines_network_graph(lines_data)
    sorted_connected_components = sorted(
        nx.connected_components(graph), key=len, reverse=True
    )

    subgraph = graph.subgraph(sorted_connected_components[1])

    # As a start (root) node, we choose the node with the highest degree
    node_degrees = subgraph.degree()
    max_degree_node = max(node_degrees, key=lambda x: x[1])[0]
    root_node = max_degree_node

    # BFS Tree
    bfs_ordered = bfs(subgraph, root_node)
    bfs_tree = nx.bfs_tree(subgraph, source=root_node)
    # DFS Tree
    dfs_ordered = dfs(subgraph, root_node)
    dfs_tree = nx.dfs_tree(subgraph, source=root_node)

    # Compare BFS and DFS
    print(f"|{'Step':<10}|{'BFS Node':<10}|{'DFS Node':<10}|")
    print(f"|{'-'*10:<10}|{'-'*10:<10}|{'-'*10:<10}|")
    for i, (bfs_node, dfs_node) in enumerate(zip(bfs_ordered, dfs_ordered)):
        print(f"|{i:<10}|{bfs_node:<10}|{dfs_node:<10}|")

    # Visualization
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    # Plot BFS Tree
    plt.subplot(121)
    pos_bfs = nx.spring_layout(bfs_tree, scale=4, seed=42)
    nx.draw(
        bfs_tree,
        pos_bfs,
        with_labels=True,
        node_size=400,
        node_color="lightcoral",
        font_size=8,
        font_color="black",
        # font_weight="bold",
        edge_color="gray",
        ax=axes[0],
    )
    # Highlight the root node with a different color
    nx.draw_networkx_nodes(
        subgraph, pos_bfs, nodelist=[root_node], node_color="coral", node_size=700
    )
    axes[0].set_title("BFS Tree")

    # Plot DFS Tree
    plt.subplot(122)
    pos_dfs = nx.spring_layout(dfs_tree, scale=4, seed=42)
    nx.draw(
        dfs_tree,
        pos_dfs,
        with_labels=True,
        node_size=400,
        node_color="lightgreen",
        font_size=8,
        font_color="black",
        edge_color="gray",
        ax=axes[1],
    )
    nx.draw_networkx_nodes(
        subgraph,
        pos_dfs,
        nodelist=[root_node],
        node_color="green",
        node_size=700,
    )
    axes[1].set_title("DFS Tree")

    plt.show()


if __name__ == "__main__":
    main()
