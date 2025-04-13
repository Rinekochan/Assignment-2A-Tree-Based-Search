from Research.dynamic_programming import dynamic_programming
from Research.genetic_algorithm import genetic_algorithm
from Research.nearest_neighbor import nearest_neighbor
from Research.research_utils import parse_args, parse_graph


def main():
    try:
        filename, method = parse_args()
        print(f"{filename} {method}")

        nodes = parse_graph(filename)
        # print(nodes)

        result = []

        match method.lower():
            case "nn":
                result, node_cnt, distance = nearest_neighbor(nodes)
            case "dp":
                result, node_cnt, distance = dynamic_programming(nodes)
            case "ga":
                result, node_cnt, distance = genetic_algorithm(nodes)
            case _:
                exit("Unknown method, available methods: BFS, DFS, GBFS, AS, CUS1, CUS2")

        print(f"Path: {result if len(result) else 'N/A'}") # last element is the goal reached
        print(f"Visited count: {node_cnt}")
        print(f"Total Distance: {distance}")


    except Exception as err:
        print(f"Unexpected {err=}")

main()
