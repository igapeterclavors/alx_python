#!/usr/bin/env python3

# def is_prime(number):
#     if number == 0:
#             return False
    
#     elif number < 0:
#             return False
#     else:
#         for i in range(2, number):
            
#                 if number % i == 0:
#                         return False
#                         break
#     return  True


def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += i
    return True
    
# print(is_prime(17))
# print(is_prime(15))
# print(is_prime(-5))
# print(is_prime(0))