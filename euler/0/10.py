#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_primes_sum(n):
    primes = get_primes_below(n)
    return sum(primes)

def get_primes_below(n):
    primes = []
    for i in range(2, n+1):
        if i % 10000 == 0:
            print("checking {0}".format(i))
        if not is_dividable(i, primes):
            primes.append(i)
    return primes

def is_dividable(n, factors):
    for f in factors:
        if n % f == 0:
            return True
    return False

print(get_primes_sum(10))
print(get_primes_sum(2000000))
