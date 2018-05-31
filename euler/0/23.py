#!/usr/bin/env python
# -*- coding: utf-8 -*-

def calculate(m):
    nums = filter(lambda n:is_non_abundant_sums(n), range(1,m+1))
    return sum(nums)

def is_non_abundant_sums(n):
    if n % 1000 == 0:
        print("processing {0}".format(n))
    for d1, d2 in iterate_divides(n):
        if get_num_type(d1) == 1 and get_num_type(d2) == 1:
            # print("{0} => {1} + {2}".format(n, d1, d2))
            return False
    return True

def iterate_divides(n):
    for i in range(1, int(n/2)+1):
        yield i, n-i

num_types = {} # cache to store num type
def get_num_type(n):
    """
    return 1 if n is an abundant number
    return 0 if n is a perfect number
    return -1 if n is deficient number
    """
    if n not in num_types:
        s = sum(get_divisors(n))
        if s < n:
            num_types[n] = -1
        if s == n:
            num_types[n] = 0
        if s > n:
            num_types[n] = 1
    return num_types[n]

def get_divisors(n):
    for factor in range(1,int(n/2)+1):
        if n % factor == 0:
            yield factor

print(calculate(100))
print(calculate(28123))
