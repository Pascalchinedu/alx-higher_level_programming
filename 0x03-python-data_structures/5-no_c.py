#!/usr/bin/python3

# A function that removes all characters c and C from a string
def no_c(my_string):

    result = []

    for word in my_string:
        # checks if string contains letter c or C
        if word != 'c' and word != 'C':
            # appends letters without c and C
            result.append(word)
    
    return ''.join(result)

# Example usage
print(no_c("Best School")) # should print "Best Shool"
print(no_c("Chicago")) # should print "hiago"
print(no_c("C is fun!")) # should print "is fun"