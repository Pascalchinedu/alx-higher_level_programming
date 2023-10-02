#!/usr/bin/python3

# A function that returns a set of common elements in two sets.
def common_elements(set_1, set_2):
    return (set_1 & set_2)


# Example
set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))