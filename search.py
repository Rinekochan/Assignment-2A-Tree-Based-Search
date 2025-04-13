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
				result, node_cnt = bfs(graph, graph.origin, graph.destinations)
			case "dfs":
				result, node_cnt = dfs(graph, graph.origin, graph.destinations)
			case "gbfs":
				result, node_cnt = gbfs(graph, graph.origin, graph.destinations)
			case "as":
				result, node_cnt = astar(graph, graph.origin, graph.destinations)
			case "cus1":
				result, node_cnt = dijkstra(graph, graph.origin, graph.destinations)
			case "cus2":
				aco = ACO(graph)
				result, node_cnt = aco.run(graph.origin, graph.destinations)
			case _:
				exit("Unknown method, available methods: BFS, DFS, GBFS, AS, CUS1, CUS2")

		print(f"{result[-1] if len(result) else 'N/A'} {node_cnt}") # last element is the goal reached
		print(result)
		total_distance = 0

		for idx in range(1, len(result)):
			total_distance += graph.adj_list[result[idx - 1]][result[idx]]

		print(f"Path Distance: {total_distance}")


	except Exception as err:
		print(f"Unexpected {err=}")

main()
