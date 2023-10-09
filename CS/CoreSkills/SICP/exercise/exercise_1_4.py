#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set sw=4 ts=4 fdm=indent fdl=0 fdn=2 ft=python et:

from __future__ import print_function, division

import operator

def a_plus_abs_b(a, b):
    return (operator.add if b > 0 else operator.sub)(a, b)

assert a_plus_abs_b(2, -2) == 4
assert a_plus_abs_b(2, 2) == 4
