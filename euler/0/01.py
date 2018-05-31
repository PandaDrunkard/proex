#!/usr/bin/env python
# -*- coding: utf-8 -*-

def sum_multiples(n):
    s = 0
    for i in range(1,n):
        if i % 3 == 0 or i % 5 == 0:
            s = s + i
    return s

print(sum_multiples(10))
print(sum_multiples(1000))
