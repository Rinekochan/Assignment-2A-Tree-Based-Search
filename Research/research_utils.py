import math
import sys
from typing import Tuple


# Parse command line arguments to retrieve graph file name and searching method
def parse_args():
    argc = len(sys.argv)
    if argc != 3:
        print("Usage: python3 research.py <filename> <method>")
        print("Methods currently supported:")
        print("\tnn - Nearest Neighbor First")
        print("\tdp - Dynamic Programming")
        print("\tga - Genetic Algorithm")
    else:
        filename = sys.argv[1]
        method = sys.argv[2]
        return filename, method

# Parse graph information from a text file
def parse_graph(filename):
    nodes = {}
    with open(filename, 'r') as file:
        current_section = None

        for line in file:
            line = line.strip()

            if not line:
                continue

            if line.startswith('Nodes:'):
                current_section = 'nodes'
                continue

            try:
                match current_section:
                    case 'nodes':
                        node_id, coords = line.split(': ')
                        coords = tuple(map(int, coords.strip('()').split(',')))
                        nodes[node_id] = coords
                    case _:
                        raise ValueError("Unknown section")
            except:
                raise IOError("Unable to read input files, please check the input format again")

    return nodes

def euclidean(cur: dict[Tuple[int]], nxt: dict[Tuple[int]]):
    cur_x, cur_y = cur.items()
    nxt_x, nxt_y = nxt.items()

    return math.sqrt((cur_x - nxt_x) ** 2 +(cur_y - nxt_y) ** 2)