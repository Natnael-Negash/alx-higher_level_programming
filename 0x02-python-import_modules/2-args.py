#!/usr/bin/python3
from sys import argv

num_argc = len(argv) - 1

def print_arguments():
    if num_argc == 0:
        print(f"{num_argc} arguments.")
    else:
        print(f"{num_argc} arguments:")
        for i in range(1,len(argv)):
            print("{:d}: {}".format(i, argv[i]))
            
if __name__ == "__main__":
    print_arguments()
