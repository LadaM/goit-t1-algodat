import csv
import re
from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx

DELIMITER = ";"
DATA_PATH = "data/linie.csv"
MAX_DECIMAL_PLACES = 1
MIN_DISTANCE = 0.1

color_map = {
    1: "#fff33b",  # yellow
    2: "#fdc70c",  # light orange
    3: "#f3903f",  # orange
    4: "#ed683c",  # red-orange
    5: "#e93e3a",  # red
}


def get_node_color(node_degree):
    if node_degree > 5:
        return color_map.get(5, "gray")
    return color_map.get(node_degree, "gray")


def print_graph_analysis(graph):
    # Print the analysis in a formatted manner
    print(f"{'Number of nodes':<40} | {graph.number_of_nodes()}")
    print(f"{'Number of edges':<40} | {graph.number_of_edges()}")
    print(
        f"{'Clustering coefficient of the graph':<40} | {nx.average_clustering(graph)}"
    )
    if nx.is_connected(graph):
        print(
            f"{'Average shortest path length':<40} | {nx.average_shortest_path_length(graph)}"
        )
    else:
        print(f"{'Average shortest path length':<40} | ---")

    print(
        f"{'Number of connected components':<40} | {nx.number_connected_components(graph)}"
    )
    print(
        f"{'Size of the largest connected component':<40} | {len(max(nx.connected_components(graph), key=len))}",
    )


def read_csv(path):
    data_points = {}
    with open(path, "r") as file:
        reader = csv.reader(file, delimiter=DELIMITER)
        count = 0
        next(reader)  # Skip the header
        for row in reader:
            data_point = {
                "line_name": row[1],
                "start_loc_name": row[2],
                "end_loc_name": row[3],
                "start_km": float(row[4]),
                "end_km": float(row[5]),
            }
            count += 1
            # storing the data point by the id of the line
            data_points[row[0]] = data_point

    return data_points


def get_short_loc_name(input_string):
    """
    Returns a shortened version of the input string based on the first three
    characters and, if the input contains spaces or hyphens, the first three
    characters and the first uppercase letter after the first three characters.
    If the input does not contain spaces or hyphens, only the first three
    characters are returned.
    For example: "Rynacht" -> "Ryn", "Erstfeld Nord Gleis" -> "ErsNG"
    :param input_string: The input string to be shortened.
    :return: The shortened version of the input string.
    """
    first_letters = input_string[:3]
    if len(re.split(r"\s|-", input_string)) > 1:
        return (first_letters + "".join(re.findall("[A-Z]", input_string)[1:]))[:5]
    else:
        return first_letters


def create_graph(data):
    """
    From data choose vertices and edges where vertex is start location or end location and edges is line name
    The weight of the edge is the inverse of the distance between the two locations (end_km-start_km).
    :param data: data is a dictionary containing the data points stored by line_id
    """
    graph = nx.Graph()
    location_short_name_by_name = {
        loc_name: get_short_loc_name(loc_name)
        for data in data.values()
        for loc_name in [data["start_loc_name"], data["end_loc_name"]]
    }
    for line_id, line_data in data.items():
        start_loc = location_short_name_by_name[line_data["start_loc_name"]]
        end_loc = location_short_name_by_name[line_data["end_loc_name"]]
        if start_loc != end_loc:  # ignore self-loops
            # distance attribute represents the distance between two points, weight is the inverse of the distance
            distance = max(
                round(line_data["end_km"] - line_data["start_km"], MAX_DECIMAL_PLACES),
                MIN_DISTANCE,
            )
            graph.add_edge(
                start_loc,
                end_loc,
                weight=(1 / distance),
                distance=distance,
                line=line_id,
            )
    return graph


def draw_graph(graph):
    pos = nx.fruchterman_reingold_layout(
        graph,
        scale=3,
        seed=42,
    )
    nx.draw(
        graph,
        pos,
        with_labels=True,
        node_size=500,
        node_color=[get_node_color(graph.degree(node)) for node in graph.nodes()],
        font_size=7,
        edge_color="gray",
    )
    edge_labels = {(u, v): d["distance"] for u, v, d in graph.edges(data=True)}
    nx.draw_networkx_edge_labels(
        graph, pos, edge_labels=edge_labels, font_color="gray", font_size=6
    )


def main():
    path_to_csv = Path.joinpath(Path(__file__).parent, DATA_PATH)
    data = read_csv(path_to_csv)

    graph = create_graph(data)
    largest_component = max(nx.connected_components(graph), key=len)
    largest_subgraph = graph.subgraph(largest_component)

    # Print the analysis
    print("\nThe network analysis:")
    print_graph_analysis(graph)
    print("\nThe largest component analysis:")
    print_graph_analysis(largest_subgraph)

    # Draw the graph
    plt.figure("Lines and Stops Network", figsize=(12, 7))
    draw_graph(largest_subgraph)
    plt.show()


if __name__ == "__main__":
    main()