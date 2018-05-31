#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_longest_chain_under(n):
    m = [-1,-1]
    for i in range(1,n):
        if i%10000 == 0:
            print("calculating {0}. Longest chain is {1}".format(i,m))
        l = get_chain_length(i)
        if l > m[1]:
            m = [i,l]
    return m

def get_chain_length(n):
    c = n
    i = 0
    while c > 1:
        #print("{0} => {1}".format(c,get_next(c)))
        c = get_next(c)
        i += 1
    return i

def get_next(n):
    if n%2 == 0:
        return int(n/2)
    else:
        return 3*n+1

print(get_longest_chain_under(1000000))
#print(calculate(1000))
