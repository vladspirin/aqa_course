"""Homework 16.1. Diamond inheritance and Geometric problem.

Create an abstract class “Shape”
with abstract methods to calculate the area and perimeter.
Inherit from it several (> 2) other shapes,
and implement mathematically correct methods
for the area and perimeter for each.
Properties such as “side length” etc.,
should be private and initialized via the constructor.
Create several different shape objects, and in a loop,
calculate and output the area and perimeter of each to the console.
"""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Abstract class Shape."""

    @abstractmethod
    def area(self):
        """Abstract method to calculate the area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method to calculate the perimeter."""
        pass


class Square(Shape):
    """A class creates the Square shape."""

    def __init__(self, side):
        """Initialize a new Square with private parameters."""
        self.__side = side

    def area(self):
        """Calculate the Square area."""
        return self.__side ** 2

    def perimeter(self):
        """Calculate the Square perimeter."""
        return 4 * self.__side


class Circle(Shape):
    """A class creates the Circle shape."""

    def __init__(self, radius):
        """Initialize a new Circle with private parameters."""
        self.__radius = radius

    def area(self):
        """Calculate the Circle area."""
        return pi * (self.__radius ** 2)

    def perimeter(self):
        """Calculate the Circle perimeter."""
        return 2 * pi * self.__radius


class Rectangle(Shape):
    """A class creates the Rectangle shape."""

    def __init__(self, length, width):
        """Initialize a new Rectangle with private parameters."""
        self.__length = length
        self.__width = width

    def area(self):
        """Calculate the Rectangle area."""
        return self.__length * self.__width

    def perimeter(self):
        """Calculate the Rectangle perimeter."""
        return 2 * (self.__length + self.__width)


class Triangle(Shape):
    """A class creates the Triangle shape."""

    def __init__(self, base, height, side1, side2):
        """Initialize a new Triangle with private parameters."""
        self.__base = base
        self.__height = height
        self.__side1 = side1
        self.__side2 = side2

    def area(self):
        """Calculate the Triangle area."""
        return 0.5 * self.__base * self.__height

    def perimeter(self):
        """Calculate the Triangle perimeter."""
        return self.__base + self.__side1 + self.__side2


if __name__ == '__main__':
    shapes = [
        Square(5),
        Circle(5),
        Rectangle(5, 4),
        Triangle(5, 4, 5, 5),
    ]
    for shape in shapes:
        print('=' * 50)
        print(f'Shape class: {shape.__class__}')
        print(f'Area: {shape.area()},  Perimeter: {shape.perimeter()}')
