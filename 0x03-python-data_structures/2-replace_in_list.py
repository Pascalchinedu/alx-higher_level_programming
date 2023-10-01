#!/usr/bin/python3

# A function that replaces an element of a list at a specific position
def replace_in_list(my_list, idx, element):

    if idx < 0:
        return (my_list)
    
    elif idx > len(my_list) - 1:
        return (my_list)
    
    else:
        my_list[idx] = element
        return (my_list)


# Example Usage
my_list = [1, 2, 3, 4, 5]
idx = 4
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)

print("{}".format(new_list))
print("{}".format(my_list))
