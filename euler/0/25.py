# -*- coding: utf-8 -*-

def calculate(n):
    

def iter_fib(sup=10*1000):
    n1 = 1
    n2 = 0
    while n2 < sup:
        next = n1 + n2
        yield next
        n1 = n2
        n2 = next

'''
1 0 1 1 2 3
'''


print(calculate(10))
print(calculate(1000))
