import os
import random


def generate_test_case(num_nodes: int, num_edges: int, max_coordinate: int, max_cost: int) -> str:
    """
    Generates a test case for the shortest path problem.

    :param num_nodes: Number of nodes in the graph.
    :param num_edges: Number of edges in the graph.
    :param max_coordinate: Maximum value for node coordinates.
    :param max_cost: Maximum weight/cost for an edge.
    :return: A formatted string containing the test case data.
    """
    nodes = {}
    edges = []

    for i in range(1, num_nodes + 1):
        x, y = random.randint(0, max_coordinate), random.randint(0, max_coordinate)
        nodes[i] = (x, y)

    # Generate all possible directed edges (excluding self-loops)
    possible_edges = [(i, j) for i in range(1, num_nodes + 1) for j in range(1, num_nodes + 1) if i != j]

    # Select a random subset of edges based on the given number of edges
    selected_edges = random.sample(possible_edges, min(num_edges, len(possible_edges)))

    for i, j in selected_edges:
        cost = random.randint(1, max_cost)
        edges.append(((i, j), cost))

    # Randomly select an origin node
    origin = random.choice(list(nodes.keys()))

    # Randomly select a subset of destination nodes (ensuring at least 1 destination)
    num_destinations = random.randint(1, num_nodes // 2)
    destinations = random.sample([n for n in nodes.keys() if n != origin], num_destinations)

    # Construct output format
    output = []
    output.append("Nodes:")
    for node, (x, y) in nodes.items():
        output.append(f"{node}: ({x},{y})")

    output.append("Edges:")
    for (i, j), cost in edges:
        output.append(f"({i},{j}): {cost}")

    output.append("Origin:")
    output.append(str(origin))

    output.append("Destinations:")
    output.append(";".join(map(str, destinations)))

    return "\n".join(output)


def generate_and_save_tests(num_tests: int, num_nodes: int, num_edges: int, max_coordinate: int, max_cost: int):
    """
    Generates multiple test cases and saves them as files in the 'Test' directory.

    :param num_tests: Number of test cases to generate.
    :param num_nodes: Number of nodes per test case.
    :param num_edges: Number of edges per test case.
    :param max_coordinate: Maximum coordinate value.
    :param max_cost: Maximum edge cost.
    """
    # Create the "Test" directory if it doesn't exist
    test_folder = "Test"
    os.makedirs(test_folder, exist_ok=True)

    # Generate and save each test case
    for i in range(1, num_tests + 1):
        test_data = generate_test_case(num_nodes, num_edges, max_coordinate, max_cost)
        file_path = os.path.join(test_folder, f"test_{i}.txt")
        with open(file_path, "w") as file:
            file.write(test_data)

        print(f"Test case {i} saved to {file_path}")


if __name__ == "__main__":
    generate_and_save_tests(num_tests=15, num_nodes=15, num_edges=30, max_coordinate=30, max_cost=20)
