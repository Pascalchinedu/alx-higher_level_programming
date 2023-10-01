#!/usr/bin/python3

# A function that finds the biggest integer of a list.
def max_integer(my_list=[]):

    largest_number = my_list[0]

    if not my_list:
        return largest_number
    
    for number in my_list[1:]:
        if number > largest_number: 
            largest_number = number
    
    return largest_number


# Example usage
my_list = [23, 436, 35, 26, 476, 387]
max_value = max_integer(my_list) # should return 476
print("Max: {}".format(max_value))
