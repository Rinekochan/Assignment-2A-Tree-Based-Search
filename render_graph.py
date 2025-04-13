import networkx as nx
import matplotlib.pyplot as plt
from utils import *
import sys
from collections import defaultdict

if len(sys.argv) != 2:
    exit("Usage: python3 render_graph.py <filename>")
graph = parse_graph(sys.argv[1])

# Create a directed graph
G = nx.DiGraph()
G.add_nodes_from(graph.nodes.keys())
G.add_weighted_edges_from([(*u, v) for u, v in graph.edges.items()])

# Just in case if nodes are in the same position (test 16)
raw_positions = graph.nodes

# Get lists of all nodes at each coordinate
groups = defaultdict(list)
for node, coord in raw_positions.items():
    groups[coord].append(node)

# Create a new position dictionary small offsets for duplicates
new_pos = {}
offset = 0.1
for coord, nodes in groups.items():
    if len(nodes) == 1:
        new_pos[nodes[0]] = coord
    else:
        # offset all nodes with same coordinates
        for i, node in enumerate(nodes):
            x, y = coord
            new_pos[node] = (x + i * offset, y + i * offset)

# Draw the graph
plt.figure(figsize=(12, 10))
nx.draw(
    G, pos=new_pos, with_labels=True, node_color='lightblue',
    node_size=800, font_size=10, arrows=True, edge_color='gray'
)

# Draw edge labels (weights)
edge_labels = {(u, v): w for (u, v), w in graph.edges.items()}
nx.draw_networkx_edge_labels(G, pos=new_pos, edge_labels=edge_labels)

plt.title("Directed Graph with Node Coordinates and Edge Weights")
plt.axis('off')
plt.tight_layout()
plt.show()
