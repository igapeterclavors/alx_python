# Write a function that prints a matrix of integers.

def print_matrix_integer(matrix=[[]]):
    for row_element in matrix:
        for column_element in row_element:
            print("{:d}".format(column_element), end=" ")
        print()  


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print_matrix_integer(matrix)
# print("--")
# print_matrix_integer()
