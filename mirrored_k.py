import matplotlib.pyplot as plt
import numpy as np

# Define vertices (points) for the lowercase "k"
vertices = np.array([
    [0, 0],  # Base point
    [0, 5],  # Top of vertical line
    [2.5, 0],  # Lower-right part of "k"
    [2, 4],  # Upper-right part of "k"
    [0, 2],  # Intersection of Vertical line
])

# List of edges (connections) between vertices
edges = [(0, 1), (4, 3), (4, 2)]


# Function to plot a "k" shape based on vertices and edges
def plot_k(points, color='black'):
    for edge in edges:
        start, end = points[edge[0]], points[edge[1]]
        plt.plot([start[0], end[0]], [start[1], end[1]], color=color)
    plt.scatter(points[:, 0], points[:, 1], color='red')  # Red dots for vertices


# Plot both the original and mirrored "k" with a gap between them
plt.figure()

# Plot the regular "k" in black
plot_k(vertices, color='black')

# Apply reflection to create a mirrored "k"
reflection_matrix = np.array([
    [-1, 0],
    [0, 1]
])

# Apply reflection transformation
mirrored_vertices = vertices @ reflection_matrix

# Shift the mirrored "k" by 1 unit to the left
shifted_mirrored_vertices = mirrored_vertices + np.array([-0.5, 0])

# Plot the shifted mirrored "k" in blue with the gap
plot_k(shifted_mirrored_vertices, color='blue')

# Set title and display both on the same axis
plt.title("lowercased k (mirrored)")
plt.axis('equal')
plt.show()
