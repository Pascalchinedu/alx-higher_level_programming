#!/usr/bin/python3



# function that deletes the item at a specific position in a list without using pop.
def delete_at(my_list=[], idx=0):

    if (idx < 0) or (idx > len(my_list) - 1):
        return my_list
    
    del my_list[idx]

    return my_list

# example usage
my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)
