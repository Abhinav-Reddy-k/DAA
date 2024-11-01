from edge_irregularity_strength import find_minimized_k_backtracking
from esg_v2 import find_minimized_k_with_time_limit
from visualize_graph import visualize_lobster_graph


def construct_amalgamated_star(n, m):
    """
    Construct the homogeneous amalgamated star graph S_{n,m} with descriptive vertex labels.

    Parameters:
    n (int): Number of outward vertices from the central node.
    m (int): Number of vertices connected to each outward vertex, including the outward vertex itself.

    Returns:
    graph (dict): A dictionary representing the graph as an adjacency list.
    """
    graph = {}

    # Central node labeled as 'C'
    center_node = 'C'
    graph[center_node] = []

    # Outward vertices (nodes connected to the central node) labeled as 'O_i' for i = 1 to n
    outward_vertices = [f'O_{i}' for i in range(1, n + 1)]

    # Add edges between center node and outward vertices
    graph[center_node] = outward_vertices

    # Add outward vertices and their star-like connections
    for i, outward_vertex in enumerate(outward_vertices, start=1):
        graph[outward_vertex] = [center_node]  # Connect to central node

        # Create m-1 additional vertices for each outward vertex, labeled 'A_i_j'
        additional_vertices = [f'A_{i}_{j}' for j in range(1, m)]
        graph[outward_vertex].extend(additional_vertices)  # Connect outward vertex to its own star vertices

        # Add the additional vertices to the graph
        for vertex in additional_vertices:
            graph[vertex] = [outward_vertex]  # Each additional vertex is connected to its outward vertex

    return graph


# Example Usage:
n = 7  # Number of outward vertices
m = 3  # Number of vertices connected to each outward vertex (including itself)
graph = construct_amalgamated_star(n, m)

# Print the adjacency list of the graph
for node, neighbors in graph.items():
    print(f"Vertex {node}: {neighbors}")

vertex_labels, minimized_k = find_minimized_k_with_time_limit(graph)

# Output results
if vertex_labels:
    print("Minimized Vertex Labels:", vertex_labels)
    print("Minimum value of k (edge irregularity strength es(G)):", minimized_k)
else:
    print("No valid labeling found.")

# Step 3: Visualize the lobster graph
if vertex_labels:
    visualize_lobster_graph(graph, vertex_labels, 'Amalgamated Star')
else:
    print("No valid labeling found.")
