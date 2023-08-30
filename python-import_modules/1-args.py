"""
Write a program that prints the number of and the list of its arguments.
"""
def my_arguments():
    if __name__ == '__main__':

        import sys

        argument = len(sys.argv)
        if argument == 1:
            print("0 arguments.")

        elif argument == 2:
            print("1 argument:")
            print("1: {}".format(sys.argv[1]))
            
        else:
            print("{} arguments:".format(argument - 1))
            for i in range(1, argument):
                print("{}: {}".format(i, sys.argv[i]))




# import sys

# def my_arguments():
#     n = len(sys.argv[1:])

#     if n == 0:
#         print("0 arguments:")

#     elif n == 1:
#         print("{} arguments:".format(n))

#         for i in range(1, len(sys.argv)):
            
#             print("{}: {}".format(i, sys.argv[i]))
#     else:
#         print("{} arguments:".format(n))

#         for i in range(1, len(sys.argv)):

#             print("{}: {}".format(i, sys.argv[i]))

# if __name__ == "__main__":
#     my_arguments()