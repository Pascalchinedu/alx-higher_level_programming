#!/usr/bin/python3

# code that prints all integers of a list
def print_list_integer(my_list=[]):
    for x in my_list:
        print("{:d}".format(x))


# Example Usage
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print_list_integer(my_list)