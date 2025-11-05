import numpy as np
import matplotlib.pyplot as plt

# Step 1: Create a 3D dataset
np.random.seed(0)
n_samples = 100
# Random 3D points with some correlation
X = np.random.multivariate_normal(
    mean=[0, 0, 0],
    cov=[[3, 1, 0.5], [1, 2, 0.3], [0.5, 0.3, 1]],
    size=n_samples
)

# Step 2: Center the data
X_centered = X - np.mean(X, axis=0)

# Step 3: Compute covariance matrix
cov_matrix = np.cov(X_centered, rowvar=False)

# Step 4: Eigen decomposition
eigvals, eigvecs = np.linalg.eigh(cov_matrix)  # symmetric matrix
# Sort eigenvalues & eigenvectors in descending order
idx = np.argsort(eigvals)[::-1]
eigvals = eigvals[idx]
eigvecs = eigvecs[:, idx]

# Step 5: Select top 2 principal components
top2_eigvecs = eigvecs[:, :2]  # shape (3,2)

# Step 6: Project data onto top 2 components
X_projected = X_centered @ top2_eigvecs  # shape (n_samples, 2)

# Step 7: Visualize
plt.figure(figsize=(8,6))
plt.scatter(X_projected[:, 0], X_projected[:, 1], color='purple', alpha=0.7)
plt.title("3D Data Projected onto 2D using PCA")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.grid(True)
plt.show()
