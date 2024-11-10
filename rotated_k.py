import matplotlib.pyplot as plt
import numpy as np

# Define vertices (points) for the lowercase "k"
vertices = np.array([
    [0, 0],  # Base point
    [0, 5],  # Top of vertical line
    [3, 0],  # Lower-right part of "k"
    [2, 4],  # Upper-right part of "k"
    [0, 2],  # Intersection of Vertical line
])

# List of edges (connections) between vertices
edges = [(0, 1), (4, 3), (4, 2)]


# Plot the lowercase "k"
def plot_k(points, color='black', title="Lowercase k"):
    plt.figure()
    for edge in edges:
        start, end = points[edge[0]], points[edge[1]]
        plt.plot([start[0], end[0]], [start[1], end[1]], color=color)
    plt.scatter(points[:, 0], points[:, 1], color='red')  # Red dots for vertices
    plt.title(title)
    plt.axis('equal')
    plt.show()


# ------STEP 2-----

# Plot the original "k"
plot_k(vertices, title="Original Lowercase k")

# Rotate "k" by 45 degrees
angle = np.radians(45)  # Convert 45 degrees to radians for rotation
rotation_matrix = np.array([
    [np.cos(angle), -np.sin(angle)],  # Rotation matrix row 1
    [np.sin(angle), np.cos(angle)]  # Rotation matrix row 2
])

# Apply rotation to each point in vertices
rotated_vertices = vertices @ rotation_matrix

# Plot the rotated "k"
plot_k(rotated_vertices, color='blue', title="k rotated (45° Counterclockwise)")
