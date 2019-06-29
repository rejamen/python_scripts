"""Python Reverse Arguments.

Given an arbitrary function, return a new function which,
when called, returns the result of the original function
called with arguments in reverse order.
"""


def original_function(a, b):
    """Function to be called with reversed args."""
    return pow(a, b)


def reversed_args(original_function):
    """Call orignal_function with reversed args."""
    return lambda *args: original_function(*args[::-1])

g = reversed_args(original_function)
print(g(2, 3))
