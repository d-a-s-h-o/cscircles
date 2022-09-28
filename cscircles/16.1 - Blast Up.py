def countup(n, c=0):
    if c == 0:
        print('Blastoff!')
    else:
        print(c)
    if n != 0:
        countup(n - 1, c + 1)
