from abc import ABC, abstractmethod
import math

# 1. Define the abstract base class `Shape`

class Shape(ABC):
    """A base class for geometric shapes."""
    
    @abstractmethod
    def get_area(self):
        
        pass

# 2. Define a child class `Square`

class Square(Shape):
    """A class representing a square."""
    
    def __init__(self, side):
        if side <= 0:
            raise ValueError("Side length must be positive.")
        self.side = side

    def get_area(self):
        """Calculates the area of the square."""
        return self.side ** 2

# 3. Define a child class `Circle`

class Circle(Shape):
    """A class representing a circle."""
    
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive.")
        self.radius = radius

    def get_area(self):
        """Calculates the area of the circle."""
        return math.pi * self.radius ** 2

# 4. Demonstrate polymorphism

def print_area_for_shape(shape_instance):
    """Takes a shape object and prints its area."""
    # The method call `shape_instance.get_area()` will execute the correct
    # implementation based on the object's actual class (Square or Circle).
    print(f"The area of the shape is: {shape_instance.get_area():.2f}")

# Create instances of the child classes
square = Square(side=5)
circle = Circle(radius=3)

# Use the generic function with different shape objects
print_area_for_shape(square)
print_area_for_shape(circle)

# You can also store the shapes in a list and iterate through them
shapes = [Square(4), Circle(2.5), Square(10)]
for shape in shapes:
    print(f"Calculating area for a {shape.__class__.__name__}:")
    print_area_for_shape(shape)
    print("-" * 30)

