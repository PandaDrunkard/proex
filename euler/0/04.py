#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_palindromic(n_s, n_e):
    n_1 = n_s
    f_1 = -1
    f_2 = -1
    f = -1
    while n_1 <= n_e:
        for n_2 in range(n_1, n_e+1):
            n = n_1 * n_2
            if is_palindromic(n) and n > f:
                f_1 = n_1
                f_2 = n_2
                f = n
        n_1 += 1
    return f, f_1, f_2

def is_palindromic(n):
    s = str(n)
    r = list(reversed(s))
    for i in range(len(s)):
        if s[i] != r[i]:
            return False
    return True

print(get_palindromic(10, 99))
print(get_palindromic(100, 999))
