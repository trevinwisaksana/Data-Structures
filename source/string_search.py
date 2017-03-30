#!python

'''
Find the starting index of the first occurrence of a pattern in a string.
'''


def find(string, pattern):
    return find_iterative(string, pattern)
    # return find_recursive(string, pattern)


def find_iterative(string, pattern):
    # number of characters in the pattern array
    length_of_pattern = len(pattern)
    # index of the current character
    current_character = 0
    # loops through each character
    for character in string:
        # character that will be compared with
        character_compared = pattern[current_character]
        # check if the current_character has compared all characters
        if character == character_compared:
            # increment after every character check
            current_character += 1
        elif character != character_compared:
            # restart the current_character index count
            current_character = 0
        # if the current_character count has been incremented enough times
        if current_character is length_of_pattern:
            return True
    return False


def find_recursive(string, pattern):
    pass


def find_index(string, pattern):
    pass


# TODO: Stretch challenge
def find_all_indexes(string, pattern):
    pass


if __name__ == '__main__':
    print(find('Treeevin', 'evin'))
