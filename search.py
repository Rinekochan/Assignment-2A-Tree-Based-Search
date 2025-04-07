from UninformedSearch.bfs import *
from UninformedSearch.dfs import *
from CustomSearch.CUS1.dijkstra import *
from utils import parse_args, parse_graph

def main():
	try:
		filename, method = parse_args()
		print(f"{filename} {method}")

		graph = parse_graph(filename)
		#print(graph)

		result = []

		for goal in graph.destinations:
			match method.lower():
				case "bfs":
					result = bfs(graph, graph.origin, goal)
				case "dfs":
					result = dfs(graph, graph.origin, goal)
				case "cus1":
					result = dijkstra(graph, graph.origin, goal)
				case "gbfs" | "as"| "cus2":
					exit(f"The method {method} is available but not implemented yet.")
				case _:
					exit("Unknown method, available methods: BFS, DFS, GBFS, AS, CUS1, CUS2")

			print(f"{goal} {len(result)}")
			print(result)


	except Exception as err:
		print(f"Unexpected {err=}")

main()
