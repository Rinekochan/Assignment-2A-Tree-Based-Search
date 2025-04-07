# Assignment 2A: Tree Based Search

## Overview

This repo contains the implement of tree-based search algorithms to solve the Route Finding Problem as part of the COS30019 - Introduction to Artificial Intelligence course. The goal of this assignment is to implement both informed and uninformed search strategies from scratch to find optimal paths between given nodes in a 2D graph.

# Objectives
- Uninformed Algorithms: Depth-First Search (DFS) and Breadth-First Search (BFS)
- Informed Algorithms: Greedy Best-First Search (GBFS) and A* Search
- Two additional custom search strategies:
    - CUS1: an uninformed algorithm
    - CUS2: an informed algorithm
- Support for text-based input files defining graph nodes, edges, and goals
- Output includes goal node, number of explored nodes and the optimal path

## Problem Description
The Route Finding Problem consists of a directed weighted graph where:
- Each node represents a location with given (x, y) coordinates.
Each edge has a cost representing the difficulty or distance to traverse between nodes.
- The goal is to find the optimal path from a given Origin and Destination

## File Format
Input files should be structured as follows:
```
Nodes:
1: (4,1)
2: (2,2)
...

Edges:
(2,1): 4
(3,1): 5
...

Origin:
2

Destinations:
5;4
```

## Search Algorithms Implemented
| **Algorithm**           | **Type**          | **Description**                                                                                                  |
|-------------------------|-------------------|------------------------------------------------------------------------------------------------------------------|
| DFS                     | Uninformed        | Explores as deep as possible before backtracking                                                                 |
| BFS                     | Uninformed        | Explores all neighbors at the current level before moving deeper                                                 |
| GBFS                    | Informed          | Selects the next node based only on heuristic cost to the goal                                                   |
| A*                      | Informed          | Uses both actual cost and heuristic cost for optimal pathfinding                                                 |
| CUS1: Dijkstra          | Uninformed Custom | Finds the shortest paths between nodes in a weighted graph                                                       |
| CUS2: Genetic Algorithm | Informed Custom   | A method for solving both constrained and unconstrained optimisation problems that is based on natural selection |

## Installation & Requirements
This project is implemented in Python. Ensure you have Python 3.10.x (or greater) installed. No external dependencies are required, since only built-in data structures are used.
### Running the Program
Execute the program via the command line:
```$ python search.py <input_file> <search_method>```

## Output format
The program prints the following results:
```
<input_file> <search_method>
<goal> <number_of_nodes_explored>
<path>
```

# Contributors
- Team name: CL1-04-Khoa-Group 05
- Team members:
    - Cao Minh Vu ([Aragami1408](https://github.com/Aragami1408))
    - Jayden Kong ([jjv7](https://github.com/jjv7))
    - Viet Hoang Pham ([Rinekochan](https://github.com/Rinekochan))
    - Cade Haynes ([CadeHaynes](https://github.com/CadeHaynes))
