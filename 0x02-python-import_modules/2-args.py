#!/usr/bin/python3
'''
    A program that prints the number of and the list of its arguments

'''
if __name__ == '__main__':
    import sys

    argv = sys.argv[1:]
    num_arg = len(argv)


    if num_arg == 0:
        '''
            Prints 0 argument if length of argument is zero
        '''
        print("0 argument" + ("" if num_arg == 1 else "s") + ".")

    else:
        '''
            Prints the length of argument and returns the 
            argument passed.
        '''
        print(f"{num_arg} argument" + ("" if num_arg == 1 else "s") + ":")

        for i, arg in enumerate(argv, start=1):
            print(f"{i}: {arg}")
