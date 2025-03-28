import sys
from dataclasses import dataclass

from uninformed import *

@dataclass
class Graph:
	nodes: dict
	edges: dict
	origin: int
	destinations: list
	adj_list: dict

# Parse command line arguments to retrieve graph file name and searching method
def parse_args():
	argc = len(sys.argv)
	if argc != 3:
		exit("Usage: python3 search.py <filename> <method>")
	else:
		filename = sys.argv[1]
		method = sys.argv[2]
		return filename, method

# Parse graph information from a text file
def parse_graph(filename):
	nodes = {}
	edges = {}
	adj_list = {}
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

			try:
				match current_section:
					case 'nodes':
						node_id, coords = line.split(': ')
						node_id = int(node_id)
						coords = tuple(map(int, coords.strip('()').split(',')))
						nodes[node_id] = coords
					case 'edges':
						edge, weight = line.split(': ')
						src, dest = map(int, edge.strip('()').split(','))
						weight = int(weight)

						# Add edge
						edges[(src, dest)] = weight

						# If adjacency lists of src does not exist, default to empty array
						adj_list.setdefault(src, []).append((dest, weight))

					case 'origin':
						origin = int(line)
					case 'destinations':
						destinations = [int(dest.strip()) for dest in line.split(';')]
					case _:
						raise ValueError("Unknown section")
			except:
				raise IOError("Unable to read input files, please check the input format again")


		graph = Graph(nodes, edges, origin, destinations, adj_list)

	return graph

def main():
	try:
		filename, method = parse_args()
		print("{} {}".format(filename, method))

		graph = parse_graph(filename)
		print(graph)

		result = []

		for goal in graph.destinations:
			match method:
				case "bfs":
					result = bfs(graph, graph.origin, goal)
				case "dfs":
					result = dfs(graph, graph.origin, goal)
				case "_":
					exit("Unknown method")

			print("{} {}".format(goal, result))


	except Exception as err:
		print(f"Unexpected {err=}")

main()
