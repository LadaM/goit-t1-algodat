import networkx as nx

from t1_network_modelling import (
    create_lines_network_graph,
    get_largest_connected_subgraph,
    get_sbb_route_network_data,
)


def main():
    # get the graph from the file t1_network_modelling.py
    lines_data = get_sbb_route_network_data()
    graph = create_lines_network_graph(lines_data)
    largest_subgraph = get_largest_connected_subgraph(graph)

    # Execute Dijkstra's algorithm for finding the shortest path
    source = "BasBB"
    target = "Eng"
    shortest_path = nx.dijkstra_path(largest_subgraph, source, target, weight="distance")
    dijkstra_path_length = nx.dijkstra_path_length(largest_subgraph, source, target, weight='distance')
    edges = nx.utils.pairwise(shortest_path)

    # sum up the distances of the edges
    edge_distances = [largest_subgraph[u][v]['distance'] for u, v in edges]
    total_distance = sum(edge_distances)

    print(total_distance == dijkstra_path_length)

    print(
        f"The shortest path is: {' -> '.join(shortest_path)} with a length of {dijkstra_path_length} km."
    )


if __name__ == "__main__":
    main()
