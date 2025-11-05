import numpy as np
import matplotlib.pyplot as plt

# Step 1: Define a grid of vectors
x = np.linspace(-2, 2, 11)  # 11 points from -2 to 2
y = np.linspace(-2, 2, 11)
X, Y = np.meshgrid(x, y)    # create a grid
points = np.vstack([X.ravel(), Y.ravel()])  # shape (2, n_points)

# Step 2: Define a transformation matrix (rotation + scaling)
theta = np.pi / 6  # 30 degrees rotation
scale_x, scale_y = 1.5, 0.5  # scaling factors
transformation_matrix = np.array([
    [scale_x*np.cos(theta), -scale_y*np.sin(theta)],
    [scale_x*np.sin(theta),  scale_y*np.cos(theta)]
])

print("Transformation Matrix:")
print(transformation_matrix)

# Step 3: Perform transformation
transformed_points = transformation_matrix @ points  # shape (2, n_points)

# Step 4: Visualize original and transformed grid
plt.figure(figsize=(8,8))
plt.scatter(points[0, :], points[1, :], color='blue', alpha=0.5, label='Original Grid')
plt.scatter(transformed_points[0, :], transformed_points[1, :], color='red', alpha=0.5, label='Transformed Grid')
plt.axis('equal')
plt.grid(True)
plt.title("Linear Transformation of 2D Vectors")
plt.xlabel("X")
plt.ylabel("Y")

# Step 5: Find eigenvectors
eigvals, eigvecs = np.linalg.eig(transformation_matrix)
print("\nEigenvalues:")
print(eigvals)
print("\nEigenvectors:")
print(eigvecs)

# Step 6: Visualize eigenvectors (scaled for visibility)
origin = np.array([[0, 0], [0, 0]])  # origin point for vectors
for i in range(eigvecs.shape[1]):
    plt.quiver(*origin[:, i], *eigvecs[:, i], color='green', scale=3, width=0.005, label=f'Eigenvector {i+1}')

plt.legend()
plt.show()
