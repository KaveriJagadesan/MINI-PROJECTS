import numpy as np
from scipy.stats import poisson
import matplotlib.pyplot as plt

# Step 1: Define parameter
# Assume historical data shows an average of 3 server crashes per month
lambda_crashes = 3  

# Step 2: Calculate probabilities
# Example: Probability of exactly 0, 1, 2, 3, 4 crashes
x_values = np.arange(0, 10)  # Number of crashes from 0 to 9
pmf_values = poisson.pmf(x_values, mu=lambda_crashes)

for x, pmf in zip(x_values, pmf_values):
    print(f"Probability of exactly {x} crashes: {pmf:.4f}")

# Probability of having at most 2 crashes (cumulative probability)
prob_at_most_2 = poisson.cdf(2, mu=lambda_crashes)
print(f"\nProbability of at most 2 crashes: {prob_at_most_2:.4f}")

# Probability of having more than 3 crashes
prob_more_than_3 = 1 - poisson.cdf(3, mu=lambda_crashes)
print(f"Probability of more than 3 crashes: {prob_more_than_3:.4f}")

# Step 3: Visualization
plt.figure(figsize=(8,5))
plt.bar(x_values, pmf_values, color='lightcoral', alpha=0.7)
plt.title("Poisson Distribution of Server Crashes per Month")
plt.xlabel("Number of Crashes")
plt.ylabel("Probability")
plt.xticks(x_values)
plt.show()

