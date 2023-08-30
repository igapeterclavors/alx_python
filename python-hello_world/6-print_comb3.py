# for i in range(1, 10):
#     for j in range(i + 1, 0):
#         print("{:02d}, ".format(i * 10 + j), end="")
#         print()


#prints all possible different combinations of two digits

for x in range(9):
    for y in range(1, 10):
        if (x == 8 and y == 9):
            print("{}{}".format(x, y))

        elif (y != x and x < y):
            print("{}{}".format(x, y), end=", ")
