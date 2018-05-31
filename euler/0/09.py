#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_pythagorean_triplet(n):
    for a in get_separated_nums(n):
        if a[0]**2 + a[1]**2 == a[2]**2:
            return a, a[0]*a[1]*a[2]
    return [-1, -1, -1]

def get_separated_nums(n):
    # select 2 numbers between 2 and n+1
    # regard them as separators
    for i in range(0, 1000*1000):
        a = [random.randint(2,n+1),random.randint(2,n+1)]
        a.sort()
        if abs(a[0]-a[1]) > 1:
            ret = [a[0]-1, a[1]-a[0]-1, n+2-a[1]]
            ret.sort()
            yield ret

print(get_pythagorean_triplet(12))
for i in range(0,5):
    print(get_pythagorean_triplet(1000))
