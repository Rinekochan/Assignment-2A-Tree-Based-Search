import sys

# Maps of nodes and edges for graph construction
nodes = {}
edges = {}
origin = None
destinations = []

def arg_parse():
	argc = len(sys.argv)
	if argc != 3:
		print('Usage: python3 search.py <filename> <method>')
	else:
		filename = sys.argv[1]
		method = sys.argv[2]

	return (filename, method)


def graph_parse(filename):
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

	return (nodes, edges, origin, destinations)

def main():
	filename, method = arg_parse()
	print("{} {}".format(filename, method));
	nodes, edges, origin, destinations = graph_parse(filename)
	print("{}\n{}\n{}\n{}".format(nodes, edges, origin, destinations))

main()
