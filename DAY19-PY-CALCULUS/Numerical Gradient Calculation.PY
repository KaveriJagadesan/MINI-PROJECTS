import numpy as np

# Sample dataset
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])  # Linear relationship: y = 2*x

# Cost function
def cost_function(params):
    w, b = params  # unpack parameters
    y_pred = w * x + b
    return np.mean((y - y_pred) ** 2)
def numerical_gradient(cost_func, params, h=1e-5):
    grad = np.zeros_like(params)
    for i in range(len(params)):
        temp_val = params[i]
        
        # forward step
        params[i] = temp_val + h
        cost_plus = cost_func(params)
        
        # backward step
        params[i] = temp_val - h
        cost_minus = cost_func(params)
        
        # partial derivative
        grad[i] = (cost_plus - cost_minus) / (2 * h)
        
        # reset parameter
        params[i] = temp_val
    return grad
initial_params = np.array([0.0, 0.0])  # starting with w=0, b=0
grad = numerical_gradient(cost_function, initial_params)
print("Numerical Gradient:", grad)
def analytical_gradient(params):
    w, b = params
    y_pred = w * x + b
    error = y - y_pred
    dw = -2 * np.mean(x * error)
    db = -2 * np.mean(error)
    return np.array([dw, db])

print("Analytical Gradient:", analytical_gradient(initial_params))
