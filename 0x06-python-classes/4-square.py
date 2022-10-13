#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initialize a new square.
        Args:
            size (int): The size of the new square
        """
        self.size = size
    
    @property
    def size(self):
        """Set the current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, width):
        if not isinstance(width, int):
            raise TypeError("size must be an integer")
        elif width < 0:
            raise ValueError("size must be >= 0")
        self.__size = width

    def area(self):
        """Return the current area of the square"""
        return (self.__size * self.__size)
