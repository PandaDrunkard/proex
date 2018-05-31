#!/usr/bin/env python
# -*- coding: utf-8 -*-

def calculate():
    a = get_factorial(100)
    s = str(a)
    ret = 0
    for i in range(0,len(s)):
        ret += int(s[i])
    return ret

def get_factorial(n):
    p = 1
    for i in range(1,n+1):
        p *= i
    return p

print(calculate())
