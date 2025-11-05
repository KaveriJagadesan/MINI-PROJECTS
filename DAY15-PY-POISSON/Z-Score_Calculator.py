import numpy as np

# Step 1: Generate a normal distribution
mu = 170      # mean
sigma = 5     # standard deviation
n_samples = 1000

data = np.random.normal(mu, sigma, n_samples)

# Step 2: Define Z-score function
def z_score(x, mean, std):
    """
    Calculate the Z-score for a given value x,
    with provided mean and standard deviation.
    """
    return (x - mean) / std

# Step 3: Pick a value from the generated data
sample_value = data[0]  # just take the first value as an example

# Step 4: Calculate Z-score
calculated_mean = np.mean(data)
calculated_std = np.std(data)

z = z_score(sample_value, calculated_mean, calculated_std)

print(f"Sample value: {sample_value:.2f}")
print(f"Calculated Mean: {calculated_mean:.2f}, Standard Deviation: {calculated_std:.2f}")
print(f"Z-score of the sample value: {z:.4f}")
# Step 5: Interpretation
if z > 0:
    print("The sample value is above the mean.")
elif z < 0:
    print("The sample value is below the mean.")
else:
    print("The sample value is equal to the mean.")