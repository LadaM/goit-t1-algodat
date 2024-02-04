import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

edges = [("A", "B"), ("A", "C"), ("B", "C"), ("C", "A"), ("D", "C")]
G.add_edges_from(edges)

pagerank = nx.pagerank(G, alpha=0.85)  # alpha is the damping factor

for node, rank in pagerank.items():
    print(f'{node}: {rank}')

plt.figure(figsize=(6, 6))
nx.draw_networkx(G, with_labels=True)
plt.show()
