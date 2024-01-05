#!/usr/bin/python3

class Rectangle:
    """
    class Rectangle that define a rectangle

    Args:
    width(int): integer
    height(int): integer

    attributes
    width(int): integer
    height(int): integer

    Raises:
      TypeError: not an integer
      ValueError: less than 0 
    """
    def __init__(self, width=0, height=0):
        self._width = width
        self.height = height

    @property    
    def width(self):
        return self._width
    @property.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError ("width must be an integer")
        if value < 0:
            raise  ValueError ("width must be >= 0")
        self.width = value
    @property
    def height(self):
        return self.height
    @property.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError ("height must be >= 0")
        self.height = value