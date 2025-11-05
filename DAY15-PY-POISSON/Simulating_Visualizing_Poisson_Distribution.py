import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Define the parameter (average arrivals per minute)
lam = 5  # λ = 5 customers per minute

# 2. Simulate arrivals over 1000 intervals
num_intervals = 1000
arrivals = np.random.poisson(lam, num_intervals)

# 3. Visualize the distribution
plt.figure(figsize=(8, 5))
sns.histplot(arrivals, bins=range(0, max(arrivals)+2), kde=False, color='skyblue', edgecolor='black')
plt.title('Poisson Distribution of Customer Arrivals (λ = 5)', fontsize=14)
plt.xlabel('Number of Customers Arriving per Minute')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# 4. Analysis
print(f"Average simulated arrivals per minute: {np.mean(arrivals):.2f}")
