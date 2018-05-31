#!/usr/bin/env python
# -*- coding: utf-8 -*-

def calculate(m):
    for i in reversed(range(0,len(m)-1)):
        for j in range(0,len(m[i])):
            d = max(m[i+1][j], m[i+1][j+1])
            m[i][j] += d
    return m[0][0]

def read_file(s):
    f = open(s)
    line = f.readline()
    m = []
    while line:
        m.append(list(map(int,line.split(' '))))
        line = f.readline()
    f.close()
    return m

m = read_file("18.txt")

print(calculate(m))
