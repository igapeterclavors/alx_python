# Write a function that prints a matrix of integers.

def print_matrix_integer(matrix=[[]]):

    for row_element in matrix:
        for column_element in row_element:

            if column_element != row_element[-1]:
                print("{:d}".format(column_element), end=" ")
            else:
                print("{:d}".format(column_element), end=" ")

            # Move to the next line after each row
        print()