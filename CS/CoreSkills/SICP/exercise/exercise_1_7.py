#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set sw=4 ts=4 fdm=indent fdl=0 fdn=2 ft=python et:

from __future__ import print_function, division

import math
# from exercise_1_6 import improve, square

def square(x) -> float:
    return x * x

def improve(guess, x) -> float:
    return (guess + x / guess) / 2.

def good_enough(guess, new_guess) -> bool:
    delta = 0.001
    return math.fabs(guess / new_guess - 1.) < delta

def sqrt_iter(guess, x) -> float:
    new_guess = improve(guess, x)
    if good_enough(guess, new_guess):
        return new_guess
    else:
        return sqrt_iter(new_guess, x)

def my_sqrt(x) -> float:
    return sqrt_iter(1., x)


print(my_sqrt(2.))
print(my_sqrt(1e2))
print(my_sqrt(1e-2))
print(my_sqrt(1e-4))
print(my_sqrt(1e4))
print(my_sqrt(1e-6))
print(my_sqrt(1e6))  # Perfectly fine!
