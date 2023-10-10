#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set sw=4 ts=4 fdm=indent fdl=0 fdn=2 ft=python et:

from __future__ import print_function, division


def p():
    return p()


def test(x, y):
    if x == 0:
        return 0
    else:
        return y


test(0, p())  # maximum recursion depth exceeded
