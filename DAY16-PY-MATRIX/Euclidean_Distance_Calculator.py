import numpy as np

# Step 1: Define the Euclidean distance function
def euclidean_distance(v1, v2):
    """
    Calculate the Euclidean distance between two vectors v1 and v2.
    """
    diff = v1 - v2               # element-wise subtraction
    sq_diff = diff ** 2           # square each element
    sum_sq_diff = np.sum(sq_diff) # sum of squares
    distance = np.sqrt(sum_sq_diff) # square root
    return distance

# Step 2: Example vectors
vector1 = np.array([2, 3, 4])
vector2 = np.array([5, 6, 7])

# Step 3: Calculate Euclidean distance
dist = euclidean_distance(vector1, vector2)
print(f"Euclidean distance between {vector1} and {vector2} is: {dist:.4f}")
