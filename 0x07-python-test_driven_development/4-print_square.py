#!/usr/bin/python3

def print_square(size):
 """
Function that prints a square with the character #

Args
size (int): integer

Raises 
TypeError
ValueError
 """
 if (not isinstance (size, int)):
      raise TypeError ("size must be an integer")
 if size < 0:
      raise ValueError ("size must be >= 0")
 if size (isinstance (size, float) and size < 0):
     raise TypeError ("size must be an integer")
 for i in range(size):
     print("#" * size)

