from uninformed import *
from custom1 import *
from informed import *
from utils import parse_args, parse_graph


def main():
	try:
		filename, method = parse_args()
		print(f"{filename} {method}")

		graph = parse_graph(filename)
		#print(graph)

		result = []

		match method.lower():
			case "bfs":
				result = bfs(graph, graph.origin, graph.destinations)
			case "dfs":
				result = dfs(graph, graph.origin, graph.destinations)
			case "cus1":
				result = dijkstra(graph, graph.origin, goal)
			case "gbfs":
				result = gbfs(graph, graph.origin, graph.destinations)
			case "as" | "cus2":
				exit(f"The method {method} is available but not implemented yet.")
			case _:
				exit("Unknown method, available methods: BFS, DFS, GBFS, AS, CUS1, CUS2")

		print(f"{result[-1]} {len(result)}") # last element is the goal reached
		print(result)


	except Exception as err:
		print(f"Unexpected {err=}")

main()
