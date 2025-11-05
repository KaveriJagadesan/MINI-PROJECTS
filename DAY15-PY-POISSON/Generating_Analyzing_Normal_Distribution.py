import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Generate Data
mu = 170        # mean
sigma = 5       # standard deviation
n_samples = 1000  # number of data points

data = np.random.normal(loc=mu, scale=sigma, size=n_samples)

# Step 2: Statistical Analysis
calculated_mean = np.mean(data)
calculated_std = np.std(data)

print(f"Calculated Mean: {calculated_mean:.2f}")
print(f"Calculated Standard Deviation: {calculated_std:.2f}")

# Empirical Rule: Count data points within 1, 2, 3 standard deviations
within_1_std = np.sum((data >= mu - sigma) & (data <= mu + sigma))
within_2_std = np.sum((data >= mu - 2*sigma) & (data <= mu + 2*sigma))
within_3_std = np.sum((data >= mu - 3*sigma) & (data <= mu + 3*sigma))

print(f"Percentage within 1 std: {within_1_std / n_samples * 100:.2f}%")
print(f"Percentage within 2 std: {within_2_std / n_samples * 100:.2f}%")
print(f"Percentage within 3 std: {within_3_std / n_samples * 100:.2f}%")

# Step 3: Visualization
plt.figure(figsize=(10,6))
sns.histplot(data, bins=30, kde=True, color='skyblue')
plt.title("Histogram of Normally Distributed Data")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.axvline(calculated_mean, color='red', linestyle='dashed', linewidth=1.5, label='Mean')
plt.legend()
plt.show()
