# Here's a Python code snippet that demonstrates the implementation of a depth-first search (DFS) algorithm for traversing a graph:


# Graph representation using an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()

        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            stack.extend(graph[vertex])

# Example usage
dfs(graph, 'A')


# In this code snippet, we represent a graph using an adjacency list.
# The graph is stored in a dictionary where the keys represent the vertices, and the values represent their adjacent vertices.

# The `dfs` function implements the depth-first search algorithm. It takes the graph and a starting vertex as input.
# The algorithm uses a stack to keep track of vertices to visit.
# It starts with the start vertex, pops a vertex from the stack, visits it, marks it as visited, and pushes its unvisited neighbors onto the stack.

# We demonstrate the usage of the `dfs` function by performing a depth-first search starting from the vertex 'A' in the example graph.
# The function prints the visited vertices in the order they are visited.

# Depth-first search is a fundamental graph traversal algorithm that can be used for various applications, such as finding connected components, detecting cycles,
#    or exploring paths in a graph.
# Understanding and implementing different graph traversal algorithms can enhance your understanding of graph data structures and their applications.