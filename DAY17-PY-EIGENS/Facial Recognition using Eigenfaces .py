import numpy as np
import matplotlib.pyplot as plt

# Step 1: Simulate loading multiple grayscale face images
# For simplicity, create random "faces" as 64x64 grayscale images
n_images = 10
img_height = 64
img_width = 64

faces = np.random.rand(n_images, img_height, img_width)  # shape (10, 64, 64)

# Step 2: Flatten each image into a vector
flattened_faces = faces.reshape(n_images, -1)  # shape (10, 4096)

# Step 3: Center the data (subtract mean face)
mean_face = np.mean(flattened_faces, axis=0)
centered_faces = flattened_faces - mean_face

# Step 4: Compute covariance matrix
# For efficiency, we can use the smaller matrix trick: cov = X*X.T
cov_matrix = np.cov(centered_faces, rowvar=False)  # shape (4096, 4096)

# Step 5: Eigen decomposition
eigvals, eigvecs = np.linalg.eigh(cov_matrix)
# Sort eigenvalues and eigenvectors in descending order
idx = np.argsort(eigvals)[::-1]
eigvals = eigvals[idx]
eigvecs = eigvecs[:, idx]

# Step 6: Visualize the top few eigenvectors as "eigenfaces"
top_k = 5
plt.figure(figsize=(12, 3))
for i in range(top_k):
    eigenface = eigvecs[:, i].reshape(img_height, img_width)
    plt.subplot(1, top_k, i+1)
    plt.imshow(eigenface, cmap='gray')
    plt.title(f"Eigenface {i+1}")
    plt.axis('off')
plt.suptitle("Top Eigenfaces")
plt.show()
# Step 7: Project original faces onto the eigenface space
projected_faces = centered_faces @ eigvecs[:, :top_k]  # shape (10, top_k)  