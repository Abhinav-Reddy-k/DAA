import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def visualize_lobster_graph(graph, labels):
    """
    Visualize the lobster graph using NetworkX and Matplotlib with improved aesthetics
    and better label positioning.

    Args:
        graph (dict): Dictionary representing the graph structure
        labels (dict): Dictionary of vertex labels
    """
    # Create figure with a larger size and white background
    plt.figure(figsize=(12, 8), facecolor='white')

    # Create graph
    G = nx.Graph()
    for vertex, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(vertex, neighbor)

    # Use kamada_kawai_layout for better node distribution
    pos = nx.kamada_kawai_layout(G)

    # Add some padding to the layout
    pos = {node: (coord[0]*1.2, coord[1]*1.2) for node, coord in pos.items()}

    # Draw edges with custom style
    nx.draw_networkx_edges(G, pos,
                           edge_color='#CCCCCC',
                           width=2,
                           alpha=0.7)

    # Draw nodes with custom style
    nx.draw_networkx_nodes(G, pos,
                           node_color='#4FB6FF',
                           node_size=700,
                           alpha=0.9,
                           linewidths=2,
                           edgecolors='white')

    # Create offset positions for vertex labels
    label_pos = {k: (v[0], v[1] + 0.08) for k, v in pos.items()}

    # Draw vertex labels with white background for better visibility
    for node, (x, y) in label_pos.items():
        plt.text(x, y,
                 f'{labels[node]}',
                 bbox=dict(facecolor='white',
                           edgecolor='none',
                           alpha=0.7,
                           pad=0.5),
                 horizontalalignment='center',
                 verticalalignment='center',
                 fontsize=10,
                 fontweight='bold')

    # Draw vertex names (numbers)
    nx.draw_networkx_labels(G, pos,
                            font_size=12,
                            font_weight='bold',
                            font_color='black')

    # Calculate edge weights
    edge_labels = {(u, v): f'{labels[u] + labels[v]}' for u, v in G.edges()}

    # Calculate and draw edge label positions
    for (node1, node2), label in edge_labels.items():
        # Get the position of both nodes
        pos1 = np.array(pos[node1])
        pos2 = np.array(pos[node2])

        # Calculate the midpoint and add a small offset
        mid_point = (pos1 + pos2) / 2
        # Calculate the perpendicular offset
        diff = pos2 - pos1
        perp = np.array([-diff[1], diff[0]]) / np.linalg.norm(diff)
        label_pos = mid_point + 0.1 * perp  # Adjust 0.1 to control label distance from edge

        # Draw edge label with white background
        plt.text(label_pos[0], label_pos[1],
                 label,
                 bbox=dict(facecolor='white',
                           edgecolor='none',
                           alpha=0.7,
                           pad=0.5),
                 horizontalalignment='center',
                 verticalalignment='center',
                 fontsize=9,
                 color='#FF4444')

    # Improve overall layout
    plt.title("Lobster Graph Visualization",
              pad=20,
              fontsize=14,
              fontweight='bold')

    # Remove axes
    plt.axis('off')

    # Add some padding around the graph
    plt.margins(0.2)

    plt.tight_layout()
    plt.show()