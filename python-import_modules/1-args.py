"""
Write a program that prints the number of and the list of its arguments.
"""
import sys

def my_arguments():
    n = len(sys.argv[1:])

    if n == 0:
        print("0 arguments:")
    elif n == 1:
        print("{} argument:".format(n))

        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
    else:
        print("{} arguments:".format(n))
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))

if __name__ == "__main__":
    my_arguments()
