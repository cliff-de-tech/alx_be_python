import math


class Shape:
    """Base class representing a geometric shape."""

    def area(self):
        """Calculate the area of the shape.
        
        Raises:
            NotImplementedError: This method should be overridden in derived classes.
        """
        raise NotImplementedError("Derived classes must override the area() method")


class Rectangle(Shape):
    """A class representing a rectangle, inheriting from Shape."""

    def __init__(self, length, width):
        """Initialize a Rectangle instance.
        
        Args:
            length (float): The length of the rectangle.
            width (float): The width of the rectangle.
        """
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of the rectangle.
        
        Returns:
            float: The area calculated as length × width.
        """
        return self.length * self.width


class Circle(Shape):
    """A class representing a circle, inheriting from Shape."""

    def __init__(self, radius):
        """Initialize a Circle instance.
        
        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """Calculate the area of the circle.
        
        Returns:
            float: The area calculated as π × radius².
        """
        return math.pi * self.radius ** 2
