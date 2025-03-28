from utils import Graph


# Breadth-first-search algorithm
# return visited array if goal is achieved, otherwise None
def bfs(graph: Graph, root: int, goal: int):
	queue = []
	visited = []

	queue.append(root)
	visited.append(root)

	while len(queue) != 0:
		node = queue.pop(0)
		for neighbor, _ in graph.adj_list[node]:
			if neighbor not in visited:
				if neighbor == goal:
					visited.append(neighbor)
					return visited
				visited.append(neighbor)
				queue.append(neighbor)

	raise ValueError("There are some problems search the path")

# Depth-first-search algorithm
# return visited array if goal is achieved, otherwise None
def dfs(graph: Graph, root: int, goal: int):
	stack = []
	visited = []

	stack.append(root)
	visited.append(root)

	while len(stack) != 0:
		node = stack.pop()
		for neighbor, _ in graph.adj_list[node]:
			if neighbor not in visited:
				if neighbor == goal:
					visited.append(neighbor)
					return visited
				visited.append(neighbor)
				stack.append(neighbor)

	raise ValueError("There are some problems search the path")

