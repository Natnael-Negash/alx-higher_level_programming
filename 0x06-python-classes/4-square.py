#!/usr/bin/python3
"""
This is a module that defines a class Square
by: (3-square.py)
"""


class Square:
    """
    This is a class that defines a Square

    Attributes:
        size (int): Length of one side of the square.
    """
    def __init__(self, size=0):
        """
        The __init__ method initializes attributes whenever an object is instantiated.

        Args:
            size (int): Length of one side of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        """
        Private instance attribute: size
        """
    def area(self):
        """
        Calculates the area of the square

        Returns:
            Area
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        Getter method that returns the size

        Returns:
            Size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method that sets the size of the square
        
        Returns:
            size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
