#!/usr/bin/env python
# -*- coding: utf-8 -*-

def calculate(factors, nth):
    factors = sorted(factors)
    for pos in iterate_positions(len(factors), nth):
        nth_pos = list(pos)
    
    return conposit_permutation(factors, nth_pos)

def iterate_positions(d, m):
    for n in range(0,m):
        ret = []
        for i in range(0,d):
            ret.append(n % (i+1))
            n = int(n / (i+1))
        yield reversed(ret)

def conposit_permutation(factors, pos):
    r = 0
    for p in pos:
        r *= 10
        r = r + factors[p]
        factors.pop(p)
    return r

factors = range(0,10)
print(calculate(factors, 1000000))
