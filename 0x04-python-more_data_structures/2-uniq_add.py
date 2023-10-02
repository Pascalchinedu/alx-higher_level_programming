#!/usr/bin/python3

'''
    A function that adds all unique integers in a list
    (only once for each integers)
'''
def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    num = 0

    for i in uniq_list:
        num += i

    return (num)


# example usage
my_list = [1, 2, 3, 1, 4, 2, 5, 12, 1, 4, 5, 6, 6, 8, 5, 9]
result = uniq_add(my_list)
print("Result: {:d}".format(result))