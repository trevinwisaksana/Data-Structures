#!python

from __future__ import print_function


def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests below
    # prevents index out of range error
    if index is not len(array):
        # used to check if the first item is the item
        if item is array[index]:
            return index
        # keeps iterating with the index value incremented
        return linear_search_recursive(array, item, index + 1)
    else:
        # if the item does not exist, it will return none
        return None


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # contains the highest value of the sliced array
    upper_index = len(array)
    # contains the lowest value of the sliced array
    lower_index = 0
    # prevents the while-loop from looping infinitely
    # bit_length finds the number of times a value can be divided by two
    max_iteration = upper_index.bit_length()
    # counts how many times the while-loop iterates
    iteration_count = 0
    # loops through to check if the item searched is in the array
    while iteration_count is not max_iteration:
        # half of the difference between the upper_index and lower_index
        difference = upper_index - lower_index
        # Retrieving the index value of the item in the middle of the array
        middle_index = (difference / 2) + lower_index
        # set the middle_item with the new middle_index value
        middle_item = array[middle_index]
        # checks if the middle_item is what we're looking for
        # doesn't work with 'is' because it only compares the characters
        if middle_item == item:
            print('Found {} at index {}'.format(item, middle_index))
            return middle_index
        # if the item has a lower ASCII value
        if item < middle_item:
            # change the upper_index
            upper_index = middle_index - 1
        # if the item has a greater ASCII value
        elif item > middle_item:
            # update the lower index
            lower_index = middle_index + 1
        # increment the count
        iteration_count += 1
    return None


def binary_search_recursive(array, item, left=None, right=None):
    # Initalizes the left and right once
    if left is None or right is None:
        # Set by default as the total number of elements
        right = len(array) - 1
        # Lower index which is zero by default
        left = 0
    # Difference
    difference = right - left
    # Index where the pointer is
    middle = (difference / 2) + left
    # Element being checked
    middle_item = array[middle]
    # Check if the middle item is the correct item
    if right < left:
        return None
    elif item == middle_item:
        return middle
    elif item < middle_item:
        return binary_search_recursive(array, item, left, middle - 1)
    elif item > middle_item:
        return binary_search_recursive(array, item, middle + 1, right)


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 1:
        target = args[0].lower()
        # names = ['Alex', 'Brian', 'Julia', 'Kojin', 'Nabil', 'Nick', 'Winnie']
        words_file = open("/usr/share/dict/words", "r")
        words = words_file.read().split()
        words_lower = [word.lower() for word in words]
        # words = words[10000:10000 + 200000]
        # for word in words:
        #     print(repr(word))
        result = binary_search(words_lower, target)
        print('binary_search({}) => {}'.format(repr(target), result))
    else:
        print('Usage: {} target'.format(sys.argv[0]))


if __name__ == '__main__':
    main()
    # names = ['Alex', 'Brian', 'Julia', 'Kojin', 'Nabil', 'Nick', 'Winnie']
    # print(binary_search(names, 'Julia'))
