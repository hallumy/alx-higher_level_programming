#!/usr/bin/python3
"""
Define a class Rectangle
"""


class Rectangle:
    """Represent a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize a new rectangle."""
        self.width = width
        self.height = height

        @property
        def height(self):
            """getter for the private instance attribute height"""
            return self.__height

        @height.setter
        def height(self, value):
            """setter for the private instance attribute height"""
            if type(value) is not int:
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value

        @property
        def width(self):
            """getter for the private instance attribute width"""
            return self.__width

        @width.setter
        def width(self, value):
            """setter for the private instance attribute width"""
            if type(value) is not int:
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value
