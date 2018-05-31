#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_nth_prime(n):
    primes = []
    i = 1
    while len(primes) < n:
        i += 1
        if not is_dividable(i, primes):
            primes.append(i)
    return primes[-1]

def is_dividable(n, factors):
    for f in factors:
        if n % f == 0:
            return True
    return False

print(get_nth_prime(5))
print(get_nth_prime(10001))
