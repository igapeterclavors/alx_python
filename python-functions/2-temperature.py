# function takes a temperature in Fahrenheit as input and returns the temperature in Celsius.

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


# print(convert_to_celsius(100))
# print(convert_to_celsius(-40))
# print(convert_to_celsius(-459.67))
# print(convert_to_celsius(32))