#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Function Divides all elements of a matrix by a given divisor.

    Args:
    matrix(list): A list of lists representing the matrix.
    div (int or float): The number to divide the elements by.

    Returns:
    list: a new matrix with all elements divided by the divisor
    """
    for row in matrix:
        if (not isinstance(row, list)):
            raise TypeError ("matrix must be a matrix (list of lists) of integers/floats")
    for element in row:
        if (not isinstance(element, int) and not isinstance(element, float)):
            raise TypeError ("matrix must be a matrix (list of lists) of integers/floats")    
    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")  
    if (not isinstance(div, int) and not isinstance(div, float)):
        raise  TypeError ("div must be a number") 
    if div == 0:
        raise  ZeroDivisionError("division by zero")
    return [[round(element / div, 2) for element in row] for row in matrix]

