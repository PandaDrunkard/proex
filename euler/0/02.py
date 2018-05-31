#!/usr/bin/env python
# -*- coding: utf-8 -*-

def sum_even_fib(n):
    f_1 = 0
    f_2 = 1
    f_3 = 1
    s = 0
    while f_3 <= n:
        if f_3 % 2 == 0:
            s += f_3
        f_1 = f_2
        f_2 = f_3
        f_3 = f_1 + f_2
    return s

print(sum_even_fib(10))
print(sum_even_fib(4000000))
