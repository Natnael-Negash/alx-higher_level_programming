#!/usr/bin/python3
from sys import argv

num_argc = len(argv) - 1

def print_arguments():
    for i in range(1,len(argv)):
        print("{:d}: {}".format(i, argv[i]))
            
if __name__ == "__main__":
     if num_argc == 0:
        print(f"{num_argc} arguments.")
    elif num_argc == 1:
        print(f"{num_argc} argument:")
    else:
        print(f"{num_argc} arguments:")
