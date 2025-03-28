import sys
from dataclasses import dataclass

@dataclass
class Graph:
	nodes: dict
	edges: dict
	origin: int
	destinations: list

# Parse command line arguments to retrieve graph file name and searching method
def parse_args():
	argc = len(sys.argv)
	if argc != 3:
		print('Usage: python3 search.py <filename> <method>')
	else:
		filename = sys.argv[1]
		method = sys.argv[2]

	return (filename, method)

# Parse graph information from a text file
def parse_graph(filename):
	nodes = {}
	edges = {}
	origin = None
	destinations = []
	graph = None
	with open(filename, 'r') as file:
		current_section = None

		for line in file:
			line = line.strip()

			if not line:
				continue

			if line.startswith('Nodes:'):
				current_section = 'nodes'
				continue
			elif line.startswith('Edges:'):
				current_section = 'edges'
				continue
			elif line.startswith('Origin:'):
				current_section = 'origin'
				continue
			elif line.startswith('Destinations:'):
				current_section = 'destinations'
				continue

			if current_section == 'nodes':
				node_id, coords = line.split(': ')
				node_id = int(node_id)
				coords = tuple(map(int, coords.strip('()').split(',')))
				nodes[node_id] = coords
			elif current_section == 'edges':
				edge, weight = line.split(': ')
				edge = tuple(map(int, edge.strip('()').split(',')))
				edges[edge] = weight
			elif current_section == 'origin':
				origin = int(line)
			elif current_section == 'destinations':
				destinations = [int(dest.strip()) for dest in line.split(';')]

		graph = Graph(nodes, edges, origin, destinations)

	return graph

def main():
	filename, method = parse_args()
	graph = parse_graph(filename)

main()
