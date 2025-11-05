import numpy as np

# Step 1: Define Inputs
input_vector = np.array([2, 3, 4])  # input for a single neuron

# Step 2: Define Weights and Bias
# 3 inputs, 2 neurons in the layer
weights_matrix = np.random.rand(3, 2)  # shape (3, 2)
bias_vector = np.array([0.1, 0.2])     # shape (2,)

print("Input Vector:")
print(input_vector)
print("\nWeights Matrix:")
print(weights_matrix)
print("\nBias Vector:")
print(bias_vector)

# Step 3: Perform Linear Transformation
linear_output = input_vector @ weights_matrix + bias_vector
print("\nLinear Output (Input @ Weights + Bias):")
print(linear_output)

# Step 4: Apply Activation Function (Sigmoid)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

activated_output = sigmoid(linear_output)
print("\nActivated Output (Sigmoid):")
print(activated_output)
