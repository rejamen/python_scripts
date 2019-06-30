"""Find appearances of given char in string."""


def find_char(s, c):
    """Arg s is the string where to find, and c is the char.

    It returns a list with all index where c was found.
    """
    print(s)
    return [i for i, ltr in enumerate(s) if ltr == c]

res = find_char('abcaabbaa', 'a')
print res
