"""Python Reverse Arguments.

Given an arbitrary function, return a new function which,
when called, returns the result of the original function
called with arguments in reverse order.
"""
import inspect
from inspect import signature


def original_function(a=2, b=3):
    """Get args a, b and do something."""
    return pow(a, b)


sig = inspect.getfullargspec(original_function)
print(sig.args)
print(sig.defaults)
reverse = sig.defaults.reverse()
print (reverse)
