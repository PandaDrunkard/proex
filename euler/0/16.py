#!/usr/bin/env python
# -*- coding: utf-8 -*-

def calculate(n):
    a = 2**n
    s = str(a)
    ret = 0
    for i in range(0,len(s)):
        ret += int(s[i])
    return ret

print(calculate(15))
print(calculate(1000))
