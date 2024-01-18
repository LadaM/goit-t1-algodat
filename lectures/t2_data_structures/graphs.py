import matplotlib.pyplot as plt
import networkx as nx

# Creating an empty graph
G = nx.Graph()

# Adding nodes
G.add_node("A")
G.add_node("B")
G.add_node("C")

# Adding edges
G.add_edge("A", "B")
G.add_edge("B", "C")

# Adding edge positions
positions = {"A": (0, 0.5), "B": (1, 0.5), "C": (2, 0.5)}

# Drawing the graph
plt.figure(figsize=(6, 6))
nx.draw_networkx(
    G,
    pos=positions,
    with_labels=True,
    font_weight="bold",
    node_color="lightblue",
    edge_color="gray",
)
plt.axis("off")
plt.show()
