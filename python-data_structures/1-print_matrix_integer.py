# Write a function that prints a matrix of integers.

def print_matrix_integer(matrix=[[]]):
    
    for row in matrix:
        for column_element in row:

            print("{:d}".format(column_element), end=" ")

            # Move to the next line after each row
        print()  

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print_matrix_integer(matrix)
# print("--")
# print_matrix_integer()
