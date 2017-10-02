"""Decode a string.

A valid code is a sequence of numbers and letter, always starting with a number
and ending with letter(s).

Each number tells you how many characters to skip before finding a good letter.
After each good letter should come the next next number.

For example, the string "hey" could be encoded by "0h1ae2bcy". This means
"skip 0, find the 'h', skip 1, find the 'e', skip 2, find the 'y'".

A single letter should work::

    >>> decode("0h")
    'h'

    >>> decode("2abh")
    'h'

Longer patterns should work::

    >>> decode("0h1ae2bcy")
    'hey'
"""

# BRUTE FORCE SOLUTION


def decode(s):
    """Decode a string."""

    # initialize
    result = ""
    index_of_digit = 0
    consumed = 0

    # loop until no letters remaining
    while consumed < len(s):
        digit = int(s[index_of_digit])
        index_of_letter = consumed + digit + 1
        result += s[index_of_letter]

        index_of_digit = index_of_letter + 1
        consumed = index_of_letter + 1

    return result

# CLEANER SOLUTION


def decode2(word):
    """Decode a string."""

    # initialize
    result = ""
    remaining = word

    while len(remaining) > 0:
        index_of_letter = int(remaining[0]) + 1
        result += remaining[index_of_letter]
        remaining = remaining[index_of_letter + 1:]
    return result

# RECURSIVE SOLUTION


def decode3(word):
    # Recursive implementation.
    # base
    if len(word) == 0:
        return ""
    # progression
    # Word is not empty.
    # KEY IDEA: Decode first letter, decode rest of input, and concatenate those
    index_of_letter = int(word[0]) + 1
    return word[index_of_letter] + decode(word[index_of_letter + 1:])

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; 0G1ar0e1ba0t2ab! ***\n"
