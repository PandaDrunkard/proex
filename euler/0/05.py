#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_num_divisible_by(n):
    ret = {}
    for i in range(1, n+1):
        prime_factors = get_prime_factors(i)
        for k in prime_factors.keys():
            if ret.get(k) == None:
                ret[k] = -1
            if ret[k] < prime_factors[k]:
                ret[k] = prime_factors[k]
    p = 1
    for k in ret.keys():
        p *= k ** ret[k]
    return p

def get_prime_factors(n):
    # number 1 has no prime factors
    if n == 1:
        return {1: 1}
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

print(get_num_divisible_by(10))
print(get_num_divisible_by(20))

# for i in range(1,50):
#     print("{0} => {1}".format(i,get_prime_factors(i)))
