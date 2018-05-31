#!/usr/bin/env python
# -*- coding: utf-8 -*-

days_of_month = {
     1: 31,
     2: 28,
     3: 31,
     4: 30,
     5: 31,
     6: 30,
     7: 31,
     8: 31,
     9: 30,
    10: 31,
    11: 30,
    12: 31,
}

def calculate():
    c = 0
    for d in iterate_days():
        if d["year"] < 1901:
            continue
        if d["year"] > 2000:
            break
        if d["day"] == 1 and d["day_of_week"] == 0:
            c += 1
    return c

def iterate_days():
    d = {"year":1900,"month":1,"day":1,"day_of_week":1}
    while True:
        if d["day"] == 1:
            print(d)
        yield d
        d = get_next_day(d)

def get_next_day(c):
    last_day = get_last_day(c["year"],c["month"])
    if c["day"] < last_day:
        # in mid of month
        c["day"] += 1
    else:
        # in end of month
        if c["month"] == 12:
            # 12/31
            c["year"] += 1
            c["month"] = 1
            c["day"] = 1
        else:
            c["month"] += 1
            c["day"] = 1
    c["day_of_week"] = get_next_day_of_week(c["day_of_week"])
    return c

def get_last_day(year,month):
    if month == 2:
        # https://en.wikipedia.org/wiki/Leap_year
        if year % 400 == 0:
            return 29
        if year % 100 == 0:
            return 28
        if year % 4 == 0:
            return 29
        return 28
    else:
        return days_of_month[month]

def get_next_day_of_week(c):
    if c > 5:
        return 0
    else:
        return c+1

print(calculate())
