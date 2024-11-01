from edge_irregularity_strength import find_minimized_k_backtracking
from esg_v2 import find_minimized_k_with_time_limit
from visualize_graph import visualize_lobster_graph


def construct_triangle_star(n):
    """
    Construct the 'Star of Triangles' graph with a center node connected to n triangles.

    Parameters:
    n (int): Number of outward nodes, each connected to a triangle.

    Returns:
    graph (dict): A dictionary representing the graph as an adjacency list.
    """
    graph = {}

    # Central node labeled 'C'
    center_node = 'C'
    graph[center_node] = []

    # Track current vertex label for the triangles
    for i in range(1, n + 1):
        # Outward node connected to the center
        outward_node = f'O_{i}'
        graph[center_node].append(outward_node)
        graph[outward_node] = [center_node]  # Connect the outward node to the central node

        # Create the two vertices forming the triangle with the outward node
        triangle_vertex_1 = f'T_{i}_1'
        triangle_vertex_2 = f'T_{i}_2'

        # Connect outward node to both triangle vertices
        graph[outward_node].extend([triangle_vertex_1, triangle_vertex_2])

        # Connect triangle vertices to form the triangle
        graph[triangle_vertex_1] = [outward_node, triangle_vertex_2]
        graph[triangle_vertex_2] = [outward_node, triangle_vertex_1]

    return graph

# Example Usage:
n = 8  # Number of outward nodes
graph = construct_triangle_star(n)

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
    visualize_lobster_graph(graph, vertex_labels, 'Star of Triangles')
else:
    print("No valid labeling found.")