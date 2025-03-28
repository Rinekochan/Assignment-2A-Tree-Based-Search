from uninformed import *
from utils import parse_args, parse_graph

def main():
	try:
		filename, method = parse_args()
		print("{} {}".format(filename, method))

		graph = parse_graph(filename)

		result = []

		for goal in graph.destinations:
			match method:
				case "BFS":
					result = bfs(graph, graph.origin, goal)
				case "DFS":
					result = dfs(graph, graph.origin, goal)
				case "_":
					exit("Unknown method, available methods: BFS, DFS, GBFS, AS, CUS1, CUS2")

			print("{} {}".format(goal, len(result)))
			print(result)


	except Exception as err:
		print(f"Unexpected {err=}")

main()
