import math

# Base Class
class Shape:
    def area(self):
        """This method should be overridden in derived classes."""
        raise NotImplementedError("Subclasses must override this method.")

# Derived Class - Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        """Initialize the Rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Override the area method to calculate the area of the rectangle."""
        return self.length * self.width

# Derived Class - Circle
class Circle(Shape):
    def __init__(self, radius):
        """Initialize the Circle with a radius."""
        self.radius = radius

    def area(self):
        """Override the area method to calculate the area of the circle."""
        return math.pi * self.radius ** 2
