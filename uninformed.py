# Breadth-first-search algorithm
# return visited array if goal is achieved, otherwise None
def bfs(graph, root, goal):
	queue = []
	visited = []

	queue.append(root)
	visited.append(root)

	while len(queue) != 0:
		node = queue.pop(0)
		for edge in graph.edges:
			a, b = edge
			if a == node and b not in visited:
				if b == goal:
					visited.append(b)
					return visited
				visited.append(b)
				queue.append(b)

	return None
