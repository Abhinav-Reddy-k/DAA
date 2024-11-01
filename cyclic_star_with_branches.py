from esg_v2 import find_minimized_k_with_time_limit
from visualize_graph import visualize_lobster_graph


def construct_cyclic_star_with_branches(n):
    """
    Construct the 'Cyclic Star with Branches' graph with a central vertex and n branches.

    Parameters:
    n (int): Number of vertices connected to the center and forming a cycle.

    Returns:
    graph (dict): A dictionary representing the graph as an adjacency list.
    """
    graph = {}

    # Central vertex labeled 'C'
    center_vertex = 'C'
    graph[center_vertex] = []

    # Create n vertices and connect them to the center and each other
    for i in range(1, n + 1):
        vertex = f'V_{i}'
        graph[vertex] = [center_vertex]  # Connect to center

        # Add two outer vertices for each vertex
        outer_vertex_1 = f'O_{i}1'
        outer_vertex_2 = f'O_{i}2'

        graph[vertex].extend([outer_vertex_1, outer_vertex_2])

        # Adding outer vertices to the graph
        graph[outer_vertex_1] = [vertex]
        graph[outer_vertex_2] = [vertex]

    # Create cyclic connections between the n vertices
    for i in range(1, n):
        graph[f'V_{i}'].append(f'V_{i + 1}')  # V_i -> V_(i+1)
        graph[f'V_{i + 1}'].append(f'V_{i}')  # V_(i+1) -> V_i
    # Closing the cycle: connect V_n back to V_1
    graph[f'V_{n}'].append('V_1')
    graph['V_1'].append(f'V_{n}')

    return graph


# Example Usage:
n = 5     # Number of vertices connected to the center
graph = construct_cyclic_star_with_branches(n)

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
    visualize_lobster_graph(graph, vertex_labels, 'Cyclic Star with Branches')
else:
    print("No valid labeling found.")
