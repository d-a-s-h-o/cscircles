primes = [True] * 1000001


def isItPrime(N):
    global primes
    primes[0] = primes[1] = False
    for i in range(2, int(N**0.5)+1):
        if primes[i]:
            for j in range(i*i, N, i):
                primes[j] = False
    return [i for i in range(N) if primes[i]]


isPrime = primes
isItPrime(1000001)
