# Write a function that removes all characters c and C from a string.

def no_c(my_string):
    new_string =''
    for char in my_string:
        if char != 'c' and char != 'C':
            new_string += char
        else:
            continue
    return new_string

print(no_c("Holberton School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))
