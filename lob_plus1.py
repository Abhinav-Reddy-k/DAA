from edge_irregularity_strength import find_minimized_k_backtracking
from esg_v2 import find_minimized_k_with_time_limit
from visualize_graph import visualize_lobster_graph


def construct_homogeneous_lobster_plus1(n, p):
    """
    Construct the Homogeneous Lobster+1 graph.

    Parameters:
    - n: Number of vertices in the path graph.
    - p: Number of vertices in each star graph (including the central vertex).

    Returns:
    - A dictionary representing the graph adjacency list.
    """
    graph = {}

    # Step 1: Create the path graph P_n
    for i in range(1, n + 1):
        graph[f'v_{i}'] = []  # Path vertices are labeled 'v_1', 'v_2', ..., 'v_n'
        if i > 1:
            # Connect consecutive vertices in the path graph
            graph[f'v_{i}'].append(f'v_{i - 1}')
            graph[f'v_{i - 1}'].append(f'v_{i}')

    # Step 2: Attach star graphs to alternate vertices in the path graph
    for i in range(2, n + 1, 2):  # Attach star graphs only to alternate vertices (2nd, 4th, etc.)
        # Create the central vertex for the first star graph attached to vertex 'v_i'
        c_1 = f'c_{i}_1'  # Central vertex for first star
        graph[c_1] = []
        graph[f'v_{i}'].append(c_1)
        graph[c_1].append(f'v_{i}')

        # Add 'p-1' leaf vertices to the first star graph
        for j in range(1, p):
            s_1 = f's_{i}_1_{j}'  # Leaf vertices for the first star
            graph[s_1] = [c_1]  # Each leaf vertex connects to the central vertex
            graph[c_1].append(s_1)

        # Create the central vertex for the second star graph attached to vertex 'v_i'
        c_2 = f'c_{i}_2'  # Central vertex for second star
        graph[c_2] = []
        graph[f'v_{i}'].append(c_2)
        graph[c_2].append(f'v_{i}')

        # Add 'p-1' leaf vertices to the second star graph
        for j in range(1, p):
            s_2 = f's_{i}_2_{j}'  # Leaf vertices for the second star
            graph[s_2] = [c_2]  # Each leaf vertex connects to the central vertex
            graph[c_2].append(s_2)

    return graph


# Example usage:
n = 3  # Number of vertices in the path graph
p = 3  # Number of vertices in each star graph (including the central vertex)

lobster_plus_one_graph = construct_homogeneous_lobster_plus1(n, p)
print(lobster_plus_one_graph.keys())

# Step 2: Find the minimized k using backtracking
vertex_labels, minimized_k = find_minimized_k_with_time_limit(lobster_plus_one_graph, 120)

# Output results
if vertex_labels:
    print("Minimized Vertex Labels:", vertex_labels)
    print("Minimum value of k (edge irregularity strength es(G)):", minimized_k)
else:
    print("No valid labeling found.")

# Step 3: Visualize the lobster graph
if vertex_labels:
    visualize_lobster_graph(lobster_plus_one_graph, vertex_labels)
else:
    print("No valid labeling found.")
