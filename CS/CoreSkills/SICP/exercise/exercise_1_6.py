#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set sw=4 ts=4 fdm=indent fdl=0 fdn=2 ft=python et:

from __future__ import print_function, division

import sys
import math
sys.setrecursionlimit(99)

def square(x):
    return x * x

def good_enough(guess, x) -> bool:
    delta = 0.001
    return math.fabs(square(guess) - x) < delta


def improve(guess, x) -> float:
    return average(guess, x / guess)


def average(x, y) -> float:
    return (x + y) / 2.


def sqrt_iter(guess, x) -> float:
    if good_enough(guess, x):
        return guess
    else:
        return sqrt_iter(improve(guess, x), x)

# Applicative order evaluation evaluates both `then_ret` and `else_ret` on
# function call, so maximum recursion depth is reached easily in Python.
def new_if(predicate, then_ret, else_ret):
    # On the other hand, `if-else`, as a special form, postpone evaluation.
    if predicate:
        return then_ret
    else:
        return else_ret


def new_sqrt_iter(guess, x) -> float:
    return new_if(
        good_enough(guess, x),
        guess,
        new_sqrt_iter(improve(guess, x), x))


def my_sqrt(x) -> float:
    return sqrt_iter(1., x)  # OK


def new_my_sqrt(x) -> float:
    return new_sqrt_iter(1., x)  # maximum recursion depth exceeded


print(my_sqrt(1e-4))
print(my_sqrt(1e4))
print(my_sqrt(2.))
print(new_my_sqrt(2.))
