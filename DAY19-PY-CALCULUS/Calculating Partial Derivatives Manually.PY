# Define the function
def f(x, y):
    return 2*x**2 + 3*x*y + y**3

# Partial derivative with respect to x
def partial_x(x, y):
    return 4*x + 3*y   # from df/dx = 4x + 3y

# Partial derivative with respect to y
def partial_y(x, y):
    return 3*x + 3*y**2   # from df/dy = 3x + 3y^2

# Test point
x_val = 1
y_val = 2

# Compute values
px = partial_x(x_val, y_val)
py = partial_y(x_val, y_val)

# Print results
print("Function value f(x,y) =", f(x_val, y_val))
print("Partial derivative wrt x (df/dx) =", px)
print("Partial derivative wrt y (df/dy) =", py)
