import math as m
L = float(input())
A = float(input())


def horizontalDistanceAfterTime(L, A):
    returns = []
    for T in range(0, 10):
        returns.append(
            L * m.cos(A * m.cos(T * m.sqrt(9.8 / L))) - L * m.cos(A))
    return returns


for i in horizontalDistanceAfterTime(L, A):
    print(i)
