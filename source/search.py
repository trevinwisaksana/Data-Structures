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
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # contains the highest value of the sliced array
    upper_index = len(array)
    # Retrieving the index value of the item in the middle of the array
    middle_index = upper_index / 2
    # Check if the item in the middle is the item looked for
    middle_item = array[middle_index]
    # prevents the while-loop from looping infinitely
    # somehow if an offset of two is not added, it won't run enough times
    max_iteration = (upper_index % 2) + 2
    # counts how many times the while-loop iterates
    iteration_count = 0
    # loops through to check if the item searched is in the array
    while item is not middle_item and iteration_count is not max_iteration:
        # increment the count
        iteration_count += 1
        # if the item has a lower ASCII value
        if item < middle_item:
            # divide the middle_index to find the middle point
            middle_index /= 2
        # if the item has a greater ASCII value
        if item > middle_item:
            # increment the middle_index by
            # half of the difference between the upper_index and middle_index
            middle_index += (upper_index - middle_index) / 2
        # set the middle_item with the new middle_index value
        middle_item = array[middle_index]
    # checks if the middle item is the one looked for
    if item is middle_item:
        return middle_index
    return None


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests below
    # Retrieving the index value of the item in the middle
    middle_index = len(array) / 2
    # retrieving the middle item
    item_searched = array[middle_index]
    # checking if the middle item is the right item
    if item is item_searched:
        return middle_index
    if item < item_searched:
        pass
    else:
        pass
    return None

if __name__ == '__main__':
    names = ['Alex', 'Brian', 'Julia', 'Kojin', 'Nabil', 'Nick', 'Winnie']
    print(binary_search(names, 'Winnie'))
