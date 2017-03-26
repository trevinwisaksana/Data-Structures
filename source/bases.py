#!python

import string


def decode(str_num, base):
    """
    Decode given number from given base to base 10.
    str_num -- string representation of number in given base
    base -- base of given number
    """
    assert 2 <= base <= 36
    # list of alphabets from a - z
    list_of_alphabets = list(string.lowercase[:26])
    # the first hex number that is alphabetized is 10
    alphabetized_hex_value = 10
    # converting the string into a list
    bits = list(str_num)  # [1, 0]
    # stores the total value
    result = 0
    # this is the power of the base depending on the bit position in the array
    # decrement = 1
    exponent = len(bits) - 1
    # iterate through the separated_number and see which base each number is
    for bit in bits:
        if bit in list_of_alphabets:
            # getting the index value of the bit
            bit_index = list_of_alphabets.index(bit)
            # adding the hex value to the index and setting it as the result
            bit = alphabetized_hex_value + bit_index
        # exponent
        # exponent = len(bits) - decrement
        # bit x (base to the power of number of bits - decrement)
        result += int(bit) * (base ** exponent)
        # increments the decrement as the loop traverses through the array
        # decrement += 1
        exponent -= 1
    return result


def encode(num, base):
    """
    Encode given number from base 10 to given base.
    num -- the number in base 10
    base -- base to convert to
    """
    assert 2 <= base <= 36
    # To store the results
    encoded = []
    while num is not 0:
        # Finding the remainder of the modulo
        remainder = num % base
        # Type casting the remainder into a string
        char_num = str(remainder)
        # 10 is the offset in the ASCII table
        if remainder >= 10:
            # Finding the ASCII number
            char_num = chr(remainder + 87)
        # Insert the char_num in the front
        encoded.insert(0, char_num)
        # Divid the num again
        num = int(num / base)

    return ''.join(encoded)


def convert(str_num, base1, base2):
    """
    Convert given number from base1 to base2.
    """
    assert 2 <= base1 <= 36
    assert 2 <= base2 <= 36
    decoded_number = decode(str_num, base1)
    result = encode(decoded_number, base2)
    return result


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        str_num = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        result = convert(str_num, base1, base2)
        print('{} in base {} is {} in base {}'.format(str_num, base1, result, base2))
    else:
        print('Usage: {} number base1 base2'.format(sys.argv[0]))


if __name__ == '__main__':
    main()
    print(decode('cab', 16))
