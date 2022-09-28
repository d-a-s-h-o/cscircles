n = int(input())


def factors_line(n):
    for i in range(1, n+1):
        if n % i == 0:
            print(f"{i} times {int(n / i)} equals {n}")


factors_line(n)
