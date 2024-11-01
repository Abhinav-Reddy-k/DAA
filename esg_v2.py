import time
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


def assign_labels_backtracking(graph, labels, used_sums, current_vertex_index, vertices, k, start_time, time_limit):
    """
    Backtracking approach to assign labels to minimize k while ensuring unique edge sums,
    with early exit if edge sums exceed possible distinct sums for current k or if time runs out.
    """
    # Check if time limit has been reached
    if time.time() - start_time > time_limit:
        return False  # Time limit exceeded

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
            if assign_labels_backtracking(graph, labels, used_sums, current_vertex_index + 1, vertices, k, start_time,
                                          time_limit):
                return True  # Found a valid labeling

            # Backtrack: Remove the edge sums and try a different label
            for edge_sum in new_sums:
                if edge_sum in used_sums:
                    used_sums.remove(edge_sum)

        # Remove the label assignment
        del labels[vertex]

    return False  # No valid label found, backtrack


def find_minimized_k_with_time_limit(graph, time_limit=90):
    """
    Perform binary search to find the minimum k (edge irregularity strength) using backtracking,
    with a specified time limit. If time runs out, return the best valid result found so far.
    """
    vertices = list(graph.keys())
    best_labels = None
    best_k = None
    labels = {}
    used_sums = set()

    # Calculate lower and upper bounds for k
    lower_bound = calculate_lower_bound(graph)
    upper_bound = len(vertices)

    start_time = time.time()

    print(f'Performing binary search for k values between {lower_bound} and {upper_bound}...')

    # Perform binary search for the minimum k
    while lower_bound <= upper_bound:
        mid_k = (lower_bound + upper_bound) // 2
        labels.clear()
        used_sums.clear()

        print(f'Trying k = {mid_k}...')

        if assign_labels_backtracking(graph, labels, used_sums, 0, vertices, mid_k, start_time, time_limit):
            # If we find a valid labeling with mid_k, try smaller k
            best_labels = labels.copy()
            best_k = mid_k
            upper_bound = mid_k - 1
            print(
                f'Found valid labeling with k = {mid_k}!, Time elapsed: {time.time() - start_time:.2f}s, Trying smaller k...')
        else:
            # If no valid labeling, increase k
            lower_bound = mid_k + 1

        # Check if time limit has been exceeded
        if time.time() - start_time > time_limit:
            print(f'Time limit of {time_limit}s exceeded.')
            break  # Stop the search if time limit is reached

    return best_labels, best_k  # Return the best labels and k found within the time limit


# Helper function to calculate lower bound
def calculate_lower_bound(graph):
    """
    Calculate a lower bound for k based on the number of edges.
    The number of possible distinct edge sums is at least the number of edges.
    """
    m = sum(len(neighbors) for neighbors in graph.values()) // 2  # Total number of edges
    lower_bound = math.ceil((m + 1) / 2)
    return lower_bound
