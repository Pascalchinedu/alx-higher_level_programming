#!/usr/bin/python3

# a fuction that retrieves an element from a list 
def element_at(my_list, idx):

    if idx < 0:
        return (None)
    elif idx > len(my_list) - 1:
        return (None)
    else:
        return (my_list[idx])
    

# Example        
my_list = [1, 2, 3, 4, 6]
idx = 5
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
# Should print: Element at index 4 is 6