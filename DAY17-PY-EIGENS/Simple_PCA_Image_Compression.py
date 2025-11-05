import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate a simple grayscale image (100x100)
# We'll use a patterned image for clarity
x = np.linspace(0, 4 * np.pi, 100)
y = np.linspace(0, 4 * np.pi, 100)
X, Y = np.meshgrid(x, y)
image = np.sin(X) + np.cos(Y)  # shape (100, 100)

plt.figure(figsize=(6,6))
plt.title("Original Image")
plt.imshow(image, cmap='gray')
plt.axis('off')
plt.show()

# Step 2: Flatten image rows (treat each row as a sample)
# Data matrix shape: (n_samples=100, n_features=100)
data = image.copy()

# Step 2a: Center the data (subtract mean of each column)
mean_cols = np.mean(data, axis=0)
data_centered = data - mean_cols

# Step 2b: Calculate covariance matrix
# Covariance shape: (n_features, n_features)
cov_matrix = np.cov(data_centered, rowvar=False)

# Step 2c: Eigen decomposition
eigvals, eigvecs = np.linalg.eigh(cov_matrix)  # use eigh for symmetric covariance
# Sort eigenvalues and eigenvectors in descending order
idx = np.argsort(eigvals)[::-1]
eigvals = eigvals[idx]
eigvecs = eigvecs[:, idx]

# Step 3: Select top k principal components
k = 20  # number of components to keep
top_eigvecs = eigvecs[:, :k]

# Step 4: Project data onto top components and reconstruct
projected_data = data_centered @ top_eigvecs   # shape (100, k)
reconstructed_data = projected_data @ top_eigvecs.T + mean_cols  # approximate original

# Step 5: Display reconstructed image
plt.figure(figsize=(6,6))
plt.title(f"Reconstructed Image with {k} Principal Components")
plt.imshow(reconstructed_data, cmap='gray')
plt.axis('off')
plt.show()
