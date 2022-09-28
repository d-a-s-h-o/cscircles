def hailstone(n):
    print(n)
    if n == 1:
        return
    elif n % 2 == 0:
        hailstone(n // 2)
    else:
        hailstone(3 * n + 1)
