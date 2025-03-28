from uninformed import *
from utils import parse_args, parse_graph

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
