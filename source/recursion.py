#!python

import unittest


def factorial(n):
    """factorial(n) returns the product of the integers 1 through n for n >= 0,
    otherwise raises ValueError for n < 0 or non-integer n"""
    # implement factorial_iterative and factorial_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return factorial_recursive(n)
    return factorial_iterative(n)


def factorial_iterative(n):
    # TODO: implement the factorial function iteratively here
    # once implemented, change factorial (above) to call factorial_iterative
    # to verify that your iterative implementation passes all tests below
    # check if n is negative or not an integer (invalid input)
    if n < 0 or not isinstance(n, int):
        raise ValueError('factorial is undefined for n = {}'.format(n))
    # check the base cases
    elif n is 0 or n is 1:
        return 1
    elif n > 1:
        # stores the result
        result = 0
        # factorial_value is decremented in every iteration
        factorial_value = n - 1
        # iterative solution
        while factorial_value is not 0:
            # result stores the multiplication
            result = n * factorial_value
            # assigning n as the new result
            n = result
            # decrementing the factorial_value
            factorial_value -= 1
        return result


def factorial_recursive(n):
    # check if n is negative or not an integer (invalid input)
    if n < 0 or not isinstance(n, int):
        raise ValueError('factorial is undefined for n = {}'.format(n))
    # check if n is one of the base cases
    elif n == 0 or n == 1:
        return 1
    # check if n is an integer larger than the base cases
    elif n > 1:
        # call function recursively
        return n * factorial_recursive(n - 1)


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 1:
        num = int(args[0])
        result = factorial(num)
        print('factorial({}) => {}'.format(num, result))
    else:
        print('Usage: {} number'.format(sys.argv[0]))


if __name__ == '__main__':
    main()
    print(factorial(3))
