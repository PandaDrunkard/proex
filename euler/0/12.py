#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_triangular_number(n):
    for t in iterate_triangular(1000000):
        factors = get_prime_factors(t)
        if get_num_of_divisors(factors) > n:
            return t
    return None

def get_num_of_divisors(d):
    ret = 1
    for v in d.values():
        ret *= v + 1
    return ret

def get_prime_factors(n):
    # number 1 has no prime factors
    if n == 1:
        return {}
    # find minimum prime factors below n/2
    ret = {}
    for factor in range(2, int(n/2) + 1):
        if n % factor == 0:
            ret = get_prime_factors(int(n/factor))
            if ret.get(factor) == None:
                ret[factor] = 0
            ret[factor] += 1
            break
    # if there is no prime factor, make it self as prime factor
    if len(ret) == 0:
        return {n:1}
    else:
        return ret

def iterate_triangular(m):
    c = 0
    for i in range(1,m+1):
        c += i
        yield c

print(get_triangular_number(5))
print(get_triangular_number(500))
