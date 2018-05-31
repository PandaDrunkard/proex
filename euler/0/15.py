#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_routes(m):
    h = len(m)
    w = len(m[0])
    m[0][0] = 1
    for i in range(0,h):
        for j in range(0,w):
            # start pos
            if i == 0 and j == 0:
                continue
            # 1st row
            if i == 0:
                m[i][j] = m[i][j-1]
                continue
            # 1st column
            if j == 0:
                m[i][j] = m[i-1][j]
                continue
            # others
            m[i][j] = m[i-1][j] + m[i][j-1]
    return m, m[h-1][w-1]

def init_matrix(h,w):
    m = []
    for i in range(0,h):
        m.append([-1] * w)
    return m

m_2_2 = init_matrix(3,3)
m_15_15 = init_matrix(21,21)

print(get_routes(m_2_2))
print(get_routes(m_15_15))
