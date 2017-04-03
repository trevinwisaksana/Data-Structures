#!python


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
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # contains the highest value of the sliced array
    upper_index = len(array)
    # contains the lowest value of the sliced array
    lower_index = 0
    # prevents the while-loop from looping infinitely
    # bit_length finds the number of times a value can be divided by two
    max_iteration = upper_index.bit_length()
    print('max_iteration', max_iteration)
    # counts how many times the while-loop iterates
    iteration_count = 0
    # loops through to check if the item searched is in the array
    while iteration_count is not max_iteration:
        print('-------------------')
        # half of the difference between the upper_index and lower_index
        difference = upper_index - lower_index
        print('difference', difference)
        # Retrieving the index value of the item in the middle of the array
        middle_index = (difference / 2) + lower_index
        print('middle_index', middle_index)
        # set the middle_item with the new middle_index value
        middle_item = array[middle_index]
        print('middle_item', middle_item)
        # checks if the middle_item is what we're looking for
        # doesn't work with 'is' because it only compares the characters
        if middle_item == item:
            print('Found {} at index {}'.format(item, middle_index))
            return middle_index
        # if the item has a lower ASCII value
        if item < middle_item:
            # change the upper_index
            upper_index = middle_index
            print('upper_index', upper_index)
            # divide the middle_index to find the middle point
            middle_index /= 2
        # if the item has a greater ASCII value
        elif item > middle_item:
            # update the lower index
            lower_index = middle_index
            print('lower_index', lower_index)
        # increment the count
        iteration_count += 1
        print('iteration_count', iteration_count)
    return None


def binary_search_recursive(array, item, left=None, right=None):
    # Initalizes the left and right once
    if left is None or right is None:
        # Set by default as the total number of elements
        right = len(array)
        # Lower index which is zero by default
        left = 0
    # Difference
    difference = right - left
    # Index where the pointer is
    pointer_index = (difference / 2) + left
    print('array value ', array[pointer_index])
    print('item value ', item)
    # Element being checked
    item_checked = array[pointer_index]
    # Check if the middle item is the correct item
    if item_checked == item:
        return pointer_index
    if item < item_checked:
        return binary_search_recursive(array, item_checked, left=left, right=pointer_index)
    elif item > item_checked:
        return binary_search_recursive(array, item_checked, left=pointer_index, right=right)


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 1:
        target = args[0]
        names = ['Alex', 'Brian', 'Julia', 'Kojin', 'Nabil', 'Nick', 'Winnie']
        # words_file = open("/usr/share/dict/words", "r")
        # array = words_file.read().split()
        # array = array[10000:10000 + 200000]
        # for word in array:
        #     print(repr(word))
        result = binary_search(names, target)
        print('binary_search({}) => {}'.format(repr(target), result))
    else:
        print('Usage: {} target'.format(sys.argv[0]))


if __name__ == '__main__':
    main()
    # names = ['Alex', 'Brian', 'Julia', 'Kojin', 'Nabil', 'Nick', 'Winnie']
    # print(binary_search(names, 'Julia'))
