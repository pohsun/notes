#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set sw=4 ts=4 fdm=indent fdl=0 fdn=2 ft=python et:

from __future__ import print_function, division

import math

def improve(guess, x) -> float:
    return (x / guess**2 + 2 * guess) / 3


def good_enough(guess, new_guess) -> bool:
    delta = 0.001
    return math.fabs(guess/new_guess - 1.) < delta


def cubert_iter(guess, x) -> float:
    new_guess = improve(guess, x)
    if good_enough(guess, new_guess):
        return new_guess
    else:
        return cubert_iter(new_guess, x)


def my_cubert(x) -> float:
    return cubert_iter(1., x)


print(my_cubert(3.))
print(my_cubert(-3.))
