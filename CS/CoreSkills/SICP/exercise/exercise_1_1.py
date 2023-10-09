#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set sw=4 ts=4 fdm=indent fdl=0 fdn=2 ft=python et:

from __future__ import print_function, division
import functools
import operator

print(10)
print(functools.reduce(operator.add, [5, 3, 4]))
print(10 - 1)
print(6 / 2)
print((2 * 4) + (4 - 6))

a = 3
b = a + 1
print(b)

def f(a, b):
    if b > a and b < a * b:
        return b
    else:
        return a
print(f(a, b))

def g(a, b):
    if a == 4:
        return 6
    elif b == 4:
        return functools.reduce(operator.add, [6, 7, a])
    else:
        return 25
print(g(a, b))

print(sum([2, b if b > a else a]))

print(functools.reduce(operator.mul, [a if a > b else b if a < b else -1, a + 1]))
