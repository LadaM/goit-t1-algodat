import networkx as nx

from t1_network_modelling import (
    create_lines_network_graph,
    get_largest_connected_subgraph,
    get_sbb_route_network_data,
    get_location_name_by_short_name,
)


def calculate_shortest_paths(graph):
    shortest_paths = {}
    # calculate the shortest path
    for source in graph.nodes():
        for target in graph.nodes():
            if source != target:
                shortest_path = nx.dijkstra_path(
                    graph, source, target, weight="distance"
                )
                shortest_path_length = nx.dijkstra_path_length(
                    graph, source, target, weight="distance"
                )
                # store the shortest_path
                shortest_paths[(source, target)] = {
                    "source": source,
                    "target": target,
                    "path": shortest_path,
                    "length": shortest_path_length,
                }
    return shortest_paths


def print_shortest_path(
    location_names, source, target, shortest_path, shortest_path_length
):
    source_name = f"{location_names[source]} ({source})"
    target_name = f"{location_names[target]} ({target})"
    path_str = "->".join(shortest_path)
    path_length_str = f"{round(shortest_path_length, 2)}km"
    print(
        f"|{source_name: <40} | {target_name: <40} | {len(shortest_path): <10} | {path_str: <70} | {path_length_str : <10}|"
    )


def main():
    # get the graph from the file t1_network_modelling.py
    lines_data = get_sbb_route_network_data()
    graph = create_lines_network_graph(lines_data)
    largest_subgraph = get_largest_connected_subgraph(graph)
    location_names = get_location_name_by_short_name(lines_data)

    shortest_paths = calculate_shortest_paths(largest_subgraph)

    print(
        f"|{'Source':<40} | {'Target':<40} | {'№ of Nodes':<10} | {'Shortest Path':<70} | {'Distance':<10}|"
        f"\n|{'-'*40} | {'-'*40} | {'-'*10} | {'-'*70} | {'-'*10}|"
    )
    for path in shortest_paths.values():
        print_shortest_path(
            location_names, path["source"], path["target"], path["path"], path["length"]
        )

    # find the shortest & longest short path by distance
    shortest_by_distance = min(shortest_paths.values(), key=lambda p: p["length"])
    longest_by_distance = max(shortest_paths.values(), key=lambda p: p["length"])
    # and by number of nodes
    shortest_by_nodes = min(shortest_paths.values(), key=lambda p: len(p["path"]))
    longest_by_nodes = max(shortest_paths.values(), key=lambda p: len(p["path"]))

    print(
        f"For graph with {largest_subgraph.number_of_nodes()} nodes and {largest_subgraph.number_of_edges()} edges."
        f"\nFound {len(shortest_paths)} shortest paths between all pairs of nodes."
        f"\nShortest path by number of nodes has {len(shortest_by_nodes['path'])} nodes"
        f"\nLongest path by number of nodes has {len(longest_by_nodes['path'])}"
        f"\nShortest path by distance is {shortest_by_distance['length']}km long"
        f"\nLongest path by distance is {longest_by_distance['length']}km long"
    )


if __name__ == "__main__":
    main()
