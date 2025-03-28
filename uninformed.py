# Breadth-first-search algorithm
# return visited array if goal is achieved, otherwise None
from utils import Graph


def bfs(graph: Graph, root, goal):
	queue = []
	visited = []

	queue.append(root)
	visited.append(root)

	while len(queue) != 0:
		cur_node = queue.pop(0)
		for node in graph.ad:
			a, b = edge
			if a == node and b not in visited:
				if b == goal:
					visited.append(b)
					return visited
				visited.append(b)
				queue.append(b)

	return None

# Depth-first-search algorithm
# return visited array if goal is achieved, otherwise None
def dfs(graph, root, goal):
	stack = []
	visited = []

	stack.append(root)
	visited.append(root)

	while len(stack) != 0:
		node = stack.pop()
		for edge in graph.edges:
			a, b = edge
			if a == node and b not in visited:
				if b == goal:
					visited.append(b)
					return visited
				visited.append(b)
				stack.append(b)

	return None

