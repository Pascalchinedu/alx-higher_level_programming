#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

def main():

    '''
       A program that imports all functions from the file calculator_1.py and handles basic operations. 

       Usage: 
            1.  If the number of arguments is not 3, your program has to:
                print Usage: ./100-my_calculator.py <a> <operator> <b> followed with a new line

                exit with the value 1

            2.  operator can be:
                + for addition
                - for subtraction
                * for multiplication
                / for division

            3.  If the operator is not one of the above:
                    print Unknown operator. Available operators: +, -, * and / followed with a new line
                exit with the value 1

            4.  You can cast a and b into integers by using int() (you can assume that all arguments will be castable into integers)

            5.  The result should be printed like this: <a> <operator> <b> = <result>, followed by a new line
    '''

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    if operator == '+':
        result = int(add(a, b))
    elif operator == '-':
        result= int(sub(a, b))
    elif operator == '*':
        result = int(mul(a, b))
    elif operator == '-':
        result = int(div(a, b))

    else:
        print("Unknown operator. Available operators: +, -, *, and /")
        sys.exit(1)
    print("{} {} {} = {}".format(a, operator, b, result))

if __name__ == '__main__':
    main()
