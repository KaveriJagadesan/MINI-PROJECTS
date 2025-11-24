import numpy as np

# Sample dataset (one feature)
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])  # true relationship y = 2*x
def cost_function(params):
    w, b = params
    y_pred = w * x + b
    return np.mean((y - y_pred) ** 2)
def numerical_gradient(cost_func, params, h=1e-5):
    grad = np.zeros_like(params)
    for i in range(len(params)):
        temp_val = params[i]
        params[i] = temp_val + h
        cost_plus = cost_func(params)
        params[i] = temp_val - h
        cost_minus = cost_func(params)
        grad[i] = (cost_plus - cost_minus) / (2 * h)
        params[i] = temp_val
    return grad
# Initialize parameters
params = np.array([0.0, 0.0])  # [w, b]
learning_rate = 0.01
iterations = 1000

for i in range(iterations):
    grad = numerical_gradient(cost_function, params)
    params -= learning_rate * grad  # update parameters
    
    if i % 100 == 0:  # print every 100 steps
        print(f"Iteration {i}, Cost: {cost_function(params):.4f}, Params: {params}")
w, b = params
print(f"Trained parameters: w = {w:.4f}, b = {b:.4f}")
