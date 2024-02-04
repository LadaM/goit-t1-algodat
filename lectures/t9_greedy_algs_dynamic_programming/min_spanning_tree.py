import networkx as nx
from heapq import heappush, heappop


def kruskal_mst(graph):
    """
    The main idea behind the Kruskal algorithm is to sort the edges based on their weight. 
    After that, we start taking edges one by one based on the lower weight. 
    If taking an edge results in forming a cycle, the edge isn't included in the MST. 
    Otherwise, the edge is included in the MST.
    Complexity: O(E * log(V))
    Works best for sparse graphs
    """
    # tree is a graph with only nodes
    forest = nx.Graph()
    for node in graph.nodes():
        forest.add_node(node)

    # sort edges in ascending order by weight
    sorted_edges = sorted(graph.edges(data=True), key=lambda t: t[2].get('weight', 1))

    mst = nx.Graph()
    # adding edges if they don't create a cycle
    for edge in sorted_edges:
        u, v, weight  = edge
        if not nx.has_path(forest, u, v):
            forest.add_edge(u, v)
            mst.add_edge(u, v, weight=weight['weight'])

    return mst



def prim_mst(graph):
    """
    Prim's algorithm is a modified version of Dijkstra's algorithm. 
    First, we choose a node to start from and add all its neighbors to a priority queue.
    After that, in each step, we extract the node that we were able to reach using the edge with the lowest weight.
    Therefore, the priority queue must contain the node and the weight of the edge that got us to reach this node.
    For each extracted node, we add it to the resulting MST and update the total cost of the MST and add all its neighbors to the queue.
    Complexity: O(E + log(V))
    Prim's algorithm is helpful when dealing with dense graphs that have lots of edges.
    """
    mst = nx.Graph()

    # select a start node
    visited = {list(graph.nodes())[0]}

    # putting all adjacent edges in the priority queue
    edges = []
    for _, v, weight in graph.edges(data='weight', nbunch=visited):
        heappush(edges, (weight, _, v))

    # while not all nodes are visited
    while visited != set(graph.nodes()):
        # choose the lightest edge connecting mst and a new node
        weight, u, v = heappop(edges)
        if v not in visited:
            # add new node to visited
            visited.add(v)
            mst.add_edge(u, v, weight=weight)
            # add all adjacent edges to the priority queue
            for _, new_v, new_weight in graph.edges(data='weight', nbunch=[v]):
                if new_v not in visited:
                    heappush(edges, (new_weight, v, new_v))

    return mst


if __name__ == '__main__':
    G = nx.Graph()
    G.add_edge('A', 'B', weight=7)
    G.add_edge('A', 'D', weight=5)
    G.add_edge('B', 'C', weight=8)
    G.add_edge('B', 'D', weight=9)
    G.add_edge('B', 'E', weight=7)
    G.add_edge('C', 'E', weight=5)
    G.add_edge('D', 'E', weight=15)
    G.add_edge('D', 'F', weight=6)
    G.add_edge('E', 'F', weight=8)
    G.add_edge('E', 'G', weight=9)
    G.add_edge('F', 'G', weight=11)

    mst_kruskal = kruskal_mst(G)
    prim_mst = prim_mst(G)
    print("Edges in the MST Kruskal:")
    for edge in mst_kruskal.edges(data=True):
        print(edge)
    
    print("Edges in the MST Prim:")
    for edge in prim_mst.edges(data=True):
        print(edge)
