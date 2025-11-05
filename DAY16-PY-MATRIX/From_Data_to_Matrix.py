import numpy as np

# Step 1: Create Raw Data
# Each student has a name, math score, and science score
raw_data = [
    ["Alice", 85, 92],
    ["Bob", 78, 88],
    ["Charlie", 90, 85],
    ["David", 72, 80]
]

# Step 2: Convert numerical data to NumPy matrix
# Extract only the scores (columns 1 and 2)
scores = np.array([row[1:] for row in raw_data])
print("Original Scores Matrix:")
print(scores)
print()

# Step 3a: Add a new feature - sports_score
sports_scores = np.array([[88], [75], [95], [70]])  # column vector
scores_with_sports = np.hstack((scores, sports_scores))
print("Matrix with Sports Scores Added:")
print(scores_with_sports)
print()

# Step 3b: Calculate a new feature - average score for each student
average_scores = np.mean(scores_with_sports, axis=1, keepdims=True)  # column vector
scores_with_avg = np.hstack((scores_with_sports, average_scores))
print("Matrix with Average Score Added:")
print(scores_with_avg)
print()

# Step 3c: Scale a feature - increase Math scores by 10%
scores_with_avg[:, 0] *= 1.1  # multiplying first column (Math) by 1.1
print("Matrix After Scaling Math Scores by 1.1:")
print(scores_with_avg)
print()
# Final Output  