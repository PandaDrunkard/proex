#!/usr/bin/env python
# -*- coding: utf-8 -*-

def calculate(n):
    s = sum(get_amicables(n))
    print(s)

def get_amicables(n):
    for i in range(1,n):
        # divisors = list(set(get_divisors(i)))
        # print("{0} => {1}".format(i, divisors))
        s1 = sum(get_divisors(i))
        s2 = sum(get_divisors(s1))
        if s2 == i and s1 != i:
            print("{0} <=> {1}".format(i,s1))
            yield i
        if i % 1000 == 0:
            print("processing {0}".format(i))

def get_divisors(n):
    for factor in range(1,int(n/2)+1):
        if n % factor == 0:
            yield factor

print(calculate(300))
print(calculate(10000))
