#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    num = number * -1
    num %= 10
    num *= -1
else:
    num = number % 10
print("Last digit of {}".format(number), end=' ')
if num > 5:
    print("is {} and is greater than 5".format(num))
elif num == 0:
    print("is {} and is 0".format(num))
else:
    print("is {} and is less than 6 and not 0".format(num))