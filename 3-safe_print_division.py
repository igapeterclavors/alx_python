"""
Write a function that divides 2 integers and prints the result.
"""

def safe_print_division(a, b):

    try:
        # enter:
        # the value 1 to a variable called a
        # the value 2 to a variable called b
        a = int(a)
        b = int(b)

        # Divide value a by value b
        division = a / b
    except ZeroDivisionError:
        pass
    finally:
        if b == 0:
            print("Inside result: {}".format(None))
        else:
            print("Inside result: {}".format(division))
            return division
