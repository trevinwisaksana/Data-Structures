#!python

# Hint: use string.ascii_letters (all letters in ASCII character set)
import string


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing"""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str)
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # changing all the characters to lowercase
    text = text.lower()
    # replacing whitespaces with no space
    text = text.replace(" ", "")
    # removing the punctionations
    text = text.translate(None, string.punctuation)
    # check if the text is empty
    if len(text) <= 1:
        return True
    # getting half of the length
    half = len(text) / 2
    # left half
    left = 0
    # right half
    right = -1
    # loops through the text
    for index in range(0, half):
        print(index)
        # first letter in the string
        first_letter = text[left]
        print(first_letter)
        # last letter in the string
        last_letter = text[right]
        print(last_letter)
        # check if the first and last letter are the same
        if first_letter is not last_letter:
            return False
        # incrimenting the left to iterate to the next letter
        print(left)
        left += 1
        # decrementing the right to iterate to the next letter
        print(right)
        right -= 1
    return True

    '''
    P.S: Four liner solution

    text = text.lower()
    if str(text) == str(text)[::-1]:
        return True
    return False

    Explanation:
    - We're checking if the string representation of n equals
      the inverted string representation of n
    - The [::-1] slice takes care of inverting the string
    - After that, we compare for equality using ==
    '''


def is_palindrome_recursive(text, left=None, right=None):
    '''
    return text[0] == text[-1] and is_palindrome_recursive(text[1:-1])
    This is inefficient because the slicing method is copying the string
    over and over again.
    '''
    if left is None and right is None:
        # changing all the characters to lowercase
        text = text.lower()
        # replacing whitespaces with no space
        text = text.replace(" ", "")
        # removing the punctionations
        text = text.translate(None, string.punctuation)
        left = 0
        right = len(text) - 1
    if left >= right:
        return True
    if text[left] is text[right]:
        return is_palindrome_recursive(text, (left + 1), (right - 1))
    return False


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            str_not = 'a' if is_pal else 'not a'
            print('{}: {} is {} palindrome'.format(result, repr(arg), str_not))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
    # print(is_palindrome_iterative('Bb'))
