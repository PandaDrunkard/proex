#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_max_prime_factor(n):
    return max(get_prime_factors(n))

def get_prime_factors(n):
    # number 1 has no prime factors
    if n == 1:
        return [1]
    # find minimum prime factors below n/2
    ret = []
    for factor in range(2, int(n/2) + 1):
        if n % factor == 0:
            ret = get_prime_factors(int(n/factor))
            ret.append(factor)
            ret = list(set(ret))
            break
    # if there is no prime factor, make it self as prime factor
    if len(ret) == 0:
        return [n]
    else:
        return ret


for i in range(1,50):
    print("{0} => {1}, max:{2}".format(i,get_prime_factors(i),get_max_prime_factor(i)))

print(get_max_prime_factor(600851475143))
