import math


def is_unique_edge_sum(vertex, graph, labels, used_sums):
    """
    Check if assigning the current label to the vertex maintains unique edge sums.
    """
    for neighbor in graph[vertex]:
        if neighbor in labels:
            edge_sum = labels[vertex] + labels[neighbor]
            if edge_sum in used_sums:
                return False  # Found a duplicate edge sum
    return True


def assign_labels_backtracking(graph, labels, used_sums, current_vertex_index, vertices, k):
    """
    Backtracking approach to assign labels to minimize k while ensuring unique edge sums.
    """
    if current_vertex_index == len(vertices):
        return True  # All vertices labeled successfully

    vertex = vertices[current_vertex_index]

    # Early pruning if we are using too many edge sums already
    if len(used_sums) > 2 * k - 1:
        return False  # Impossible to have unique sums with this k

    # Try assigning each label from 1 to k
    for label in range(1, k + 1):
        labels[vertex] = label

        # Check if the edge sums are unique
        if is_unique_edge_sum(vertex, graph, labels, used_sums):
            # Temporarily add the new edge sums
            new_sums = []
            for neighbor in graph[vertex]:
                if neighbor in labels:
                    edge_sum = labels[vertex] + labels[neighbor]
                    new_sums.append(edge_sum)
                    used_sums.add(edge_sum)

            # Recurse to the next vertex
            if assign_labels_backtracking(graph, labels, used_sums, current_vertex_index + 1, vertices, k):
                return True  # Found a valid labeling

            # Backtrack: Remove the edge sums and try a different label
            for edge_sum in new_sums:
                used_sums.remove(edge_sum)

        # Remove the label assignment
        del labels[vertex]

    return False  # No valid label found, backtrack

# Helper function to calculate lower bound
def calculate_lower_bound(graph):
    """
    Calculate a lower bound for k based on the number of edges.
    The number of possible distinct edge sums is at least the number of edges.
    """
    m = sum(len(neighbors) for neighbors in graph.values()) // 2  # Total number of edges
    lower_bound = math.ceil((m + 1) / 2)
    return lower_bound


def find_minimized_k_backtracking(graph, start_k=None):
    """
    Find the minimum k (edge irregularity strength) using backtracking.
    """
    vertices = list(graph.keys())
    labels = {}
    used_sums = set()

    if not start_k:
        start_k = calculate_lower_bound(graph)

    # Start with k = number of vertices (upper bound), and reduce k step by step
    for k in range(start_k, len(vertices) + 1):
        print(f'Trying k = {k}...')
        if assign_labels_backtracking(graph, labels, used_sums, 0, vertices, k):
            return labels, k  # Found a valid labeling with minimum k

    return None, None  # No valid solution found
