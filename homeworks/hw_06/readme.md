# Graph Analysis and Visualization

I decided to take the real-world data and to analyse it. This decision cost me a lot of time. Data that I was using can be found and downloaded [here](https://data.sbb.ch/explore/dataset/linie/information/?location=7,47.67648,9.38232&basemap=00c4d6). The dataset represents the lines of the SBB railway network in Switzerland. I've downloaded the csv file which is stored at `hw_06/data/linie.csv`

## Modelling
### Data Selection & Preparation
I've selected the following information from the dataset to include into the model of the graph:
* `line_id` - for identifying the individual lines
* `line_name` - just in case I wanted it later for representation purposes
* `start_loc_name` - starting location (node) of the line
* `end_loc_name` - end location (node) of the line
* `start_km` - where the line starts
* `end_km` - where the line ends
### Graph Design
* Edges
  * Line represents an edge in the graph
  * The edge doesn't have a direction
    * every edge is bidirectional
    * if there is a line between location A and B, we can get A --> B and B --> A
  * The lines connecting location to itself were ignored
* Nodes
  * Start and end locations represent the nodes that are connected by the line
    * The names of the locations were shortened to serve as node label 
* Edge Attributes
  * The distance between the `start_km` and `end_km` represents the `distance` between two nodes
  * `weight` of the edge is the inverse of the `distance` 
    * positioning algorithms that consider `weight` interpret larger weight as stronger connection
    * the nodes with 'stronger' connection are drawn closer to each other

## Visualisation
The visualization was the hardest part of the task. Choosing the layout that makes graph more or less readable is a challenge.
* `nx.spring_layout()` was chosen to position the nodes and edges, choosing the `scale` that would produce the best spaced out result was a matter of great patience
* `seed=42` was provided to make the generated visualization more stable
* the edges are labeled with `distance` between two locations (or nodes)
* the color of the node depends on the number of outgoing (incoming) edges -- the _degree_ of the node
  * the closer to red -- the higher degree
![img.png](largest_subgraph.png)
## Analysis
For the whole graph :
1. Number of nodes = **567**
2. Number of edges = **415**
3. Clustering coefficient of the graph = ~ **0.0034**
4. Average shortest path length - not defined for the graph that is not connected
5. Number of connected components = **155**
6. Size of the largest connected component = **63**

For the largest connected subgraph:
1. Number of nodes = **63**
2. Number of edges = **65**
3. Clustering coefficient of the graph = ~ **0.0313**
4. Average shortest path length - ~ **5.67**

We can see that:
* The clustering coefficient for the connected subgraph is 10 times higher than for the whole graph that is not connected
* Number of edges is significantly smaller than number of nodes in the graph that is not connected

## BFS & DFS
For creating the table of visits to the nodes, the standard implementations of the BFS and DFS were used:
* `bfs(graph)` uses a `queue` to visit the neighbors and only then the children
* `dfs(graph)` uses s `stack` to go deep and visit the children first
### The sequence of visiting the nodes
> From the table of visits of specific locations (nodes), we can see that at every step except the first one (the root node), the visited nodes are different

| Step | BFS Node | DFS Node |
|------|----------|----------|
| 0    | Do       | Do       |
| 1    | Klo      | IsT      |
| 2    | ZuON     | Lau      |
| 3    | Rib      | GeA      |
| 4    | Aro      | InO      |
| 5    | DoII     | GrG      |
| 6    | IsT      | Gri      |
| 7    | Hu       | Zwe      |
| 8    | Gr       | MoMOB    |
| 9    | PoB      | LeS      |
| 10   | ChGRB    | Aig      |
| 11   | Leg      | AiD      |
| 12   | Lau      | LeGH     |
| 13   | Sis      | MoV      |
| 14   | LoSA     | DoII     |
| 15   | GrG      | Aro      |
| 16   | InO      | Leg      |
| 17   | GeA      | ChGRB    |
| 18   | Olt      | Rib      |
| 19   | LoFAR    | PoB      |
| 20   | Gri      | LoSA     |
| 21   | WoSBB    | LoFAR    |
| 22   | Bie      | ZuON     |
| 23   | Zwe      | Gr       |
| 24   | Da       | Sis      |
| 25   | Mor      | Olt      |
| 26   | LeS      | Bie      |
| 27   | MoMOB    | Mor      |
| 28   | LeLF     | LeLF     |
| 29   | Aig      | ChN      |
| 30   | ChN      | Pr       |
| 31   | MoV      | Da       |
| 32   | AiD      | WoSBB    |
| 33   | Pr       | Hu       |
| 34   | LeGH     | Klo      |

### Visualisation of DFS- & BFS-Tree
* The root node is larger and brighter
* From the tree representation it is difficult to say which algorithm was used for building it
![img.png](trees.png)

## Dijkstra 
I've run the `nx.dijkstra_path()` for all nodes of the largest interconnected subgraph. Here are the key points of the analysis:
* 63 nodes and 65 edges
* Found 3906 shortest paths between all pairs of nodes
* Shortest path by number of nodes has 2 nodes
* Longest path by number of nodes has 15
* Shortest path by distance is 0.1km long
* Longest path by distance is 391.4km long
