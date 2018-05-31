#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_sum_square_difference(n):
    n_sum = sum(range(1, n+1))**2
    n_squre = sum(map(squre, range(1, n+1)))
    return n_sum - n_squre

def squre(n):
    return n**2

print(get_sum_square_difference(10))
print(get_sum_square_difference(100))
