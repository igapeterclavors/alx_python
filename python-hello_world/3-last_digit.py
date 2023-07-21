#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


if number < 0:
    new = number * -1
    last_digit = -1 * ( new % 10)
else:
    new = number
    last_digit = new % 10

if lastDigit > 5:
    print("Last digit is greater than 5".format(number, last_digit))
elif lastDigit < 0:
    print("Last digit is less than 6 and not 0".format(number, last_digit))
else:
    print("Last digit is 0".format(number, last_digit))
