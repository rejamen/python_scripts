"""Print the first non primes n numbers."""


def factorial(n):
    """Return n!."""
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


def is_prime(n):
    """Return True is n is a prime number."""
    # if (n - 1)! + 1 is divisible by n, then n is a prime number
    n_factorial = factorial(n - 1)
    n_factorial += 1
    res = False
    if n > 1 and n_factorial % n == 0:
        res = True
    return res


def positive_number_generator():
    """Return the generator."""
    n = 1
    while True:
        x = yield n
        if x is not None:
            n = x
        else:
            n += 1


def manipulate_generator(g, n):
    """Something."""
    pass


k = (int)(raw_input("Number: "))
g = positive_number_generator()
for _ in range(k):
    n = next(g)
    print n
    manipulate_generator(g, n)
