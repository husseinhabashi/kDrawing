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
plt.figure()
for edge in edges:
    start, end = vertices[edge[0]], vertices[edge[1]]
    plt.plot([start[0], end[0]], [start[1], end[1]], 'k-')
plt.scatter(vertices[:, 0], vertices[:, 1], color='red')
plt.title("Lowercase k")
plt.axis('equal')
plt.show()
