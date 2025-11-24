import numpy as np

# Function
def f(x):
    return x**4 - 3*x**3 + 2

# Derivative
def df(x):
    return 4*x**3 - 9*x**2

# Gradient Descent
def gradient_descent(start_x, lr=0.01, max_iter=10000, tol=1e-6):
    x = start_x
    for i in range(max_iter):
        grad = df(x)
        new_x = x - lr * grad

        # Stop when gradient is very small
        if abs(grad) < tol:
            print(f"Converged in {i} iterations")
            return new_x

        x = new_x
    return x

# Start at a random value
start = np.random.uniform(-3, 3)
print("Starting x:", start)

min_x = gradient_descent(start)
print("Estimated minimum at x =", min_x)
print("Function value f(x) =", f(min_x))
