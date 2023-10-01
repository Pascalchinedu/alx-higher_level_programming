#!/usr/bin/python3

# a function that replaces an element in a list at a specific position without modifying the original list.
def new_in_list(my_list, idx, element):

    new_list = my_list[:]

    if idx < 0:
        return (None)
    
    elif idx > len(my_list) -1:
        return (None)
    
    else:
        new_list[idx] = element
        return (new_list)
    
# Example
my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print("New list: {}".format(new_list)) # should print new_list
print("My list: {}".format(my_list)) # should print my_list
