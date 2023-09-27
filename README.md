# Applied-Optimization Labs within Linköping university
**Lab1- Fondamentals** 

This Optimization Lab, explores fundamental concepts in graph theory and optimization. It covers various aspects,
including graph visualization using NetworkX and Matplotlib, adjacency matrix representation, queue operations, and topological sorting algorithms.

**Lab 2: Shortest Paths**

Question 1: Unweighted Single-Source Shortest Paths
- The lab begins by defining a Graph class to represent a directed graph and to facilitate graph-related operations.
- It implements breadth-first search (BFS) to find unweighted single-source shortest paths in the graph.
- An example graph is created and paths from a source vertex to all other vertices are calculated and displayed.

Question 2: Positive Weighted Single-Source Shortest Paths
- The lab introduces Dijkstra's algorithm for finding positive weighted single-source shortest paths in a directed graph.
- A Dijkstra class is defined, which includes methods to calculate the shortest paths, set and get properties for vertices, and determine the path from a source vertex to other vertices.
- An example weighted graph is provided, and the shortest paths from a source vertex ('5') to all other vertices are computed and presented.
This lab provides a practical exploration of unweighted and weighted single-source shortest path algorithms, offering insights into their implementation and complexity.

**Lab3- Minimum Spanning Tree (Kruskal's Algorithm)**
- Implementation of Kruskal's Algorithm to find the minimum spanning tree of a given graph
- Definition of a Graph class for creating and managing graphs
- Functions for adding edges, searching for precedents or parents of nodes, and handling the union operation
- Application of Kruskal's Algorithm to the graph, sorting edges by weight, and systematically adding them to the minimum spanning tree
- Presentation of the resulting minimum spanning tree and its total weight
- Practical exercise providing hands-on experience with Kruskal's Algorithm and optimization in graph theory.

**Lab4-Linear Programming and Assignment Problem Solvers**
It tackles two problems:

### Linear Programming Problem

**Problem Description**

- Linear programming aims to maximize a linear objective function while adhering to linear constraints.
- For example:
  - Maximize: 2x + 3y
  - Constraints:
    1. x + y ≤ 4
    2. x ≥ 1
    3. y ≥ 2
    4. x, y ≥ 0

**Usage**

- For solving the linear programming problem, we utilize the **PuLP** library.
- You can install PuLP via pip: pip install pulp

- The script will display:
  - The status of the solution.
  - The optimal values of the decision variables.
  - The optimal objective value.

### Assignment Problem

**Problem Description**

- The assignment problem addresses the optimal allocation of workers to tasks, minimizing costs.
- In our example, we use a 4x4 cost matrix representing worker-task assignments.

**Usage**

- To address the assignment problem, we employ the **Gurobi** library.
- You can obtain Gurobi by following the installation instructions on their official website.
- The script will present:
  - The optimal assignment of workers to tasks.
  - The total cost of the assignment.
