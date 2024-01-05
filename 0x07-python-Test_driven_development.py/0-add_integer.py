#!/usr/bin/python3

def add_integer(a, b=98):
    """ 
    Fuction to add floats or integers

    args
    a(number) : float or integer
    b(number) : float or integer

    Raises
    Type error: if not float or integer

    Returns
    float:int: float or integer
    """
    if (not isinstance (a,int) and not isinstance(a,float)):
        raise TypeError("a must be integer")
    if (not isinstance (b,int) and not isinstance (b,float)):
        raise TypeError("b must be integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b