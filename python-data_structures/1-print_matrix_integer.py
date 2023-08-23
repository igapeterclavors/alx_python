# Write a function that prints a matrix of integers. 

def print_matrix_integer(matrix=[[]]):
    for row_element in matrix:
        i = 1
        if len(row_element) == 0:
            print("")
        else:
            for column_element in row_element:
                if i < len(row_element):
                    print("{:d}".format(column_element), end=" ")
                else:
                    print("{:d}".format(column_element), end="\n")
                i += 1

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print_matrix_integer(matrix)
# print("--")
# print_matrix_integer()
