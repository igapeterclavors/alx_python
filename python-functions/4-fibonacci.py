#!/usr/bin/env python3

def fibonacci_sequence(n):
    x = 0
    y = 1
    series = []
    if n == 1:
        series.append(x)
    if n >= 2:
        series.append(x)
        series.append(y)
    if n == 2:
        series.append(x)
        series.append(y)
    while (n > 2):
        allTotal = x + y
        series.append(allTotal)
        x = y
        y = allTotal
        n -=1
    return series