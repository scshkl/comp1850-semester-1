# Week 1.6, Session 1: Task 3

import math
from point import Point

VALID_COLOURS = {"red", "orange", "yellow", "green", "blue", "purple"}


class Shape:
    """
    Superclass for different types of shape.
    """

    def __init__(self, position, colour):
        """
        Creates a shape with the specified position & colour.
        """
        self.set_position(position)
        self.set_colour(colour)

    def set_position(self, position):
        """
        Moves this shape to the given position.
        """
        if not isinstance(position, Point):
            raise TypeError("position must be a Point")

        self.position = position

    def set_colour(self, colour):
        """
        Sets this shape's colour to the given colour.
        """
        if colour not in VALID_COLOURS:
            raise ValueError(f"invalid color: must be one of {VALID_COLOURS}")

        self.colour = colour


# Implement your Circle class here
# Make sure that it inherits properly from Shape!
class Circle(Shape):
    def __init__(self, radius, position, colour="red"):
        super().__init__(position, colour)
        self.set_radius(radius)

    def set_radius(self, radius):
        if not isinstance(radius, (int, float)):
            raise TypeError("radius needs to be a number")

        if radius <= 0:
            raise ValueError("radius needs to be greater than 0")
        
        self.radius = radius

    def __str__(self):
        # red circle, radius 2.5, at (0.0, 0.0)
        return f"{self.colour} circle, radius {self.radius}, at {self.position}"

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius
