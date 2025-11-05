import numpy as np

# Step 1: Create a sample 2D dataset (rows = samples, columns = features)
# Example: 4 samples, 3 features (Math, Science, Sports scores)
M = np.array([
    [85, 92, 88],
    [78, 88, 75],
    [90, 85, 95],
    [72, 80, 70]
])

print("Original Matrix:")
print(M)

# Step 2: Compute mean and standard deviation for each feature (column-wise)
mean_features = M.mean(axis=0)
std_features = M.std(axis=0)

print("\nFeature-wise Mean:")
print(mean_features)
print("\nFeature-wise Std Dev:")
print(std_features)

# Step 3: Scale the dataset
M_scaled = (M - mean_features) / std_features

print("\nScaled Matrix (Zero Mean, Unit Variance per Feature):")
print(M_scaled)
