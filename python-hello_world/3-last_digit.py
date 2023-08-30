#!/usr/bin/python3
# import random

# number = random.randint(-10000, 10000)

# last_digit = abs(number) % 10

# print("The string Last digit of", number, "is", last_digit, end=" ")

# if last_digit > 5:
#     print("and the number is greater than 5")
# elif last_digit == 0:
#     print("the number is 0")
# else:
#     print("and it is less than 6 and not 0")



#
import random

number = random.randint(-10000, 10000)

if number < 0:
    print("Last digit of {0} is {1} and is less than 6 and not 0".format(number, -(-number % 10)))
    
else:
    if (number % 10) > 5:
        print("Last digit of {0} is {1} and is greater than 5".format(number, (number % 10)))
        
    elif (number % 10) == 0:
        print("Last digit of {0} is {1} and is 0".format(number, (number % 10)))
        
    elif (number % 10) < 6:
        print("Last digit of {0} is {1} and is less than 6 and not 0".format(number, (number % 10)))