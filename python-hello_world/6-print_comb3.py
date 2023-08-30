#prints all possible different combinations of two digits
for x in range(9):
    for y in range(1, 10):
        if (x == 8 and y == 9):
            print("{}{}".format(x, y))
        elif (y != x and x < y):
            print("{}{}".format(x, y), end=", ")
