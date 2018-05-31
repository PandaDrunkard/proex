#!/usr/bin/env python
# -*- coding: utf-8 -*-

def calculate(names):
    names = sorted(names, key=str.lower)
    print(sum(iterate(names)))

def iterate(names):
    for i in range(0,len(names)):
        print([names[i], get_name_worth(names[i])])
        yield (i+1) * get_name_worth(names[i])

def get_name_worth(name):
    return sum(map(get_char_worth, name))

def get_char_worth(c):
    return ord(c.lower()) - 96

def read_file(s):
    f = open(s)
    line = f.readline()
    names = line.split(',')
    for n in names:
        yield n.replace('"','')
    f.close()

names = list(set(read_file("22.txt")))
print(calculate(names))
