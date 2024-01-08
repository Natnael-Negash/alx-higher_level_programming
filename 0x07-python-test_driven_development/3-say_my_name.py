#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
     """
     Function that prints My name is <first_name> <last_name>

     Args 
      first_name (string)
      last_name (string: optional)

    Raises 
     TypeError: if not string
     """
     if(not isinstance (first_name, str) or not isinstance (last_name, str)):
         raise TypeError("first_name and last_name must be a string" )
     print(f"My name is {first_name} {last_name}")



