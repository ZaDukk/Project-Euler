from math import isqrt
import random

#sive of eratosthenes
def primesLessThan(n):
    if n<= 2:
        return []
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, isqrt(n)+1):
        if is_prime[i]:
            for x in range(i*i, n, i):
                is_prime[x] = False

    return [i for i in range(n) if is_prime[i]]

#Miller-Rabin primality test
def isPrime(n):
    if n <= 1:
        return False

    def _miller_rabin_pass(a, s, d, n):
        a_to_power = pow(a, d, n)
        if a_to_power == 1:
            return True
        for _ in range(s - 1):
            if a_to_power == n - 1:
                return True
            a_to_power = (a_to_power * a_to_power) % n
        return a_to_power == n - 1

    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1

    for _ in range(20):
        a = 0
        while a == 0:
            a = random.randrange(n)
        if not _miller_rabin_pass(a, s, d, n):
            return False
    return True

