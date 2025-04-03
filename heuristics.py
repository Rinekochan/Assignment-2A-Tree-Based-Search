from utils import *
import math
def pythagoras(graph: Graph, goal: str):
	result = {}
	goal_x, goal_y = graph.nodes[goal]

	for node in graph.nodes.keys():
		start_x, start_y = graph.nodes[node]
		dist = math.sqrt(pow(goal_x - start_x, 2) + pow(goal_y - start_y, 2))
		result[node] = dist

	return result
