#!/usr/bin/python3

'''
A function that finds all multiples of 2 in a list.
Returns a new list with True or False, depending on whether the interger at the same position in the original list is a multiple of 2
The new list should have the same original size as the original list
'''
def divisible_by_2(my_list=[]):

    new_list = []
    # iterates through length of list
    for i in range(len(my_list)):
        # checks if current integer is divisible by 2
        if i % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)

    return new_list

# example usage 
my_list = [0, 1, 2, 3, 4, 5, 6]

print(my_list) # should return [True, False, True, False, True, False, True]
print(divisible_by_2(my_list))
