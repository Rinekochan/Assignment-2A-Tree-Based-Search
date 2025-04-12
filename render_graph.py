import networkx as nx
import matplotlib.pyplot as plt
from utils import *
import sys

if len(sys.argv) != 2:
    exit("Usage: python3 render_graph.py <filename>")
graph = parse_graph(sys.argv[1])

# Create a directed graph
G = nx.DiGraph()
G.add_nodes_from(graph.nodes.keys())
G.add_weighted_edges_from([(u, v, w) for (u, v), w in graph.edges])

# Draw the graph
plt.figure(figsize=(12, 10))
nx.draw(
    G, pos=graph.nodes, with_labels=True, node_color='lightblue',
    node_size=800, font_size=10, arrows=True, edge_color='gray'
)

# Draw edge labels (weights)
edge_labels = {(u, v): w for (u, v), w in graph.edges}
nx.draw_networkx_edge_labels(G, pos=graph.nodes, edge_labels=edge_labels)

plt.title("Directed Graph with Node Coordinates and Edge Weights")
plt.axis('off')
plt.tight_layout()
plt.show()
