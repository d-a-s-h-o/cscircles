import math as m


def choose(n, k):
    return m.factorial(n) // m.factorial(k) // m.factorial(n - k)
