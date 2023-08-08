""" 
Write a program that imports the function def add(a, b): 
from the file and prints the result of the addition 1 + 2 = 3 
"""

# importing add module
from add_0 import add

# defining function my_add to add two numbers
def my_add():

# assign:
# the value 1 to a variable called a
# the value 2 to a variable called b
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
if __name__ == "__main__":
    my_add()