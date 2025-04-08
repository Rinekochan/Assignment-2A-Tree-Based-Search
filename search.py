from UninformedSearch.bfs import *
from UninformedSearch.dfs import *
from InformedSearch.gbfs import *
from InformedSearch.astar import *
from CustomSearch.CUS1.dijkstra import *
from CustomSearch.CUS2.aco import *

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
			case "gbfs":
				result = gbfs(graph, graph.origin, graph.destinations)
			case "as":
				result = astar(graph, graph.origin, graph.destinations)
			case "cus1":
				result = dijkstra(graph, graph.origin, graph.destinations)
			case "cus2":
				aco = ACO(graph)
				result = aco.run(graph.origin, graph.destinations)
			case _:
				exit("Unknown method, available methods: BFS, DFS, GBFS, AS, CUS1, CUS2")

		if len(result) and graph.origin in graph.destinations:
			print(f"{result[-1]} {len(result)}") # last element is the goal reached
		else:
			print(f"{graph.destinations} N/A")
		print(result)


	except Exception as err:
		print(f"Unexpected {err=}")

main()
