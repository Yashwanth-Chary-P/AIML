# Check if the color can be assigned to the given node
def is_safe(node, graph, colors, color):
    # Check all adjacent nodes
    for neighbor in range(len(graph)):
        if graph[node][neighbor] == 1 and colors[neighbor] == color:
            return False
    return True


# Backtracking function
def graph_coloring_util(graph, m, colors, node):
    # If all nodes are colored, return True
    if node == len(graph):
        return True

    # Try different colors
    for color in range(1, m + 1):
        if is_safe(node, graph, colors, color):
            # Assign color
            colors[node] = color

            # Recur for next node
            if graph_coloring_util(graph, m, colors, node + 1):
                return True

            # Backtrack (remove color)
            colors[node] = 0

    return False


# Main function
def graph_coloring(graph, m):
    n = len(graph)

    # Store colors of nodes (0 means not colored)
    colors = [0] * n

    # Call the utility function
    if not graph_coloring_util(graph, m, colors, 0):
        print("No solution exists")
        return False

    # Print solution
    print("Solution exists:")
    for i in range(n):
        print(f"Node {i} ---> Color {colors[i]}")

    return True


# Driver Code
if __name__ == "__main__":
    # Adjacency Matrix of Graph
    graph = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0]
    ]

    # Number of colors
    m = 3

    graph_coloring(graph, m)