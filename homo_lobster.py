from edge_irregularity_strength import find_minimized_k_backtracking
from esg_v2 import find_minimized_k_with_time_limit
from visualize_graph import visualize_lobster_graph


def construct_lobster_graph(n, p):
    # Initialize an empty adjacency list for the graph
    adjacency_list = {}

    # Path graph vertices: v_1, v_2, ..., v_n
    path_vertices = [f'v_{i + 1}' for i in range(n)]

    # Add path vertices to the adjacency list
    for vertex in path_vertices:
        adjacency_list[vertex] = []

    # Create edges for the path graph P_n
    for i in range(n - 1):
        # Connect v_i with v_{i+1}
        adjacency_list[path_vertices[i]].append(path_vertices[i + 1])
        adjacency_list[path_vertices[i + 1]].append(path_vertices[i])

    # For each path vertex, add its two unique star graphs
    for i, vertex in enumerate(path_vertices):
        # First star graph S_{p,i}^1
        c_1 = f'c_{i + 1}_1'  # Central vertex of the first star graph
        adjacency_list[c_1] = []
        adjacency_list[vertex].append(c_1)
        adjacency_list[c_1].append(vertex)

        # Add the outer vertices of the first star graph
        for j in range(p - 1):
            outer_vertex = f's_{i + 1}_1_{j + 1}'
            adjacency_list[outer_vertex] = []
            adjacency_list[c_1].append(outer_vertex)
            adjacency_list[outer_vertex].append(c_1)

        # Second star graph S_{p,i}^2
        c_2 = f'c_{i + 1}_2'  # Central vertex of the second star graph
        adjacency_list[c_2] = []
        adjacency_list[vertex].append(c_2)
        adjacency_list[c_2].append(vertex)

        # Add the outer vertices of the second star graph
        for j in range(p - 1):
            outer_vertex = f's_{i + 1}_2_{j + 1}'
            adjacency_list[outer_vertex] = []
            adjacency_list[c_2].append(outer_vertex)
            adjacency_list[outer_vertex].append(c_2)

    return adjacency_list


# Example usage:
n = 2  # Number of vertices in the path graph
p = 4  # Number of vertices in each star graph (including the central vertex)

# Step 1: Construct the graph
lobster_graph = construct_lobster_graph(n, p)

for vertex, neighbors in lobster_graph.items():
    print(f'{vertex}: {neighbors}')

# Step 2: Find the minimized k using backtracking
vertex_labels, minimized_k = find_minimized_k_with_time_limit(lobster_graph)

# Output results
if vertex_labels:
    print("Minimized Vertex Labels:", vertex_labels)
    print("Minimum value of k (edge irregularity strength es(G)):", minimized_k)
else:
    print("No valid labeling found.")

# Step 3: Visualize the lobster graph
if vertex_labels:
    visualize_lobster_graph(lobster_graph, vertex_labels, 'Lobster Graph')
else:
    print("No valid labeling found.")
