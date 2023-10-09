#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set sw=4 ts=4 fdm=indent fdl=0 fdn=2 ft=python et:

from __future__ import print_function, division
import functools
import operator

ladd = functools.partial(functools.reduce, operator.add)
lsub = functools.partial(functools.reduce, operator.sub)
lmul = functools.partial(functools.reduce, operator.mul)
ldiv = functools.partial(functools.reduce, operator.truediv)

def f(x, y, z):
    def larger(a, b):
        return a if a > b else b
    def smaller(a, b):
        return a if a < b else b
    def square(a):
        return a * a

    return ladd([
        square(larger(x, y)),
        square(larger(z, smaller(x, y)))
    ])

assert f(0, 2, 2) == 8
assert f(1, 2, 3) == 13
assert f(3, 5, 7) == 74
