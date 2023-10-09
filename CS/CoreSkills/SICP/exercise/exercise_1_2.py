#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set sw=4 ts=4 fdm=indent fdl=0 fdn=2 ft=python et:

from __future__ import print_function, division
import functools
import operator

a = functools.reduce(operator.truediv, [
    functools.reduce(operator.add, [
        5,
        4,
        functools.reduce(operator.sub, [
            2,
            functools.reduce(operator.sub,[
                3,
                functools.reduce(operator.add,[
                    6,
                    functools.reduce(operator.truediv,[
                        4,
                        5
                    ])
                ])
            ])
        ])
    ]),
    functools.reduce(operator.mul, [
        3,
        functools.reduce(operator.sub, [
            6,
            2
        ]),
        functools.reduce(operator.sub, [
            2,
            7
        ])
    ])
])
print(a)

ladd = functools.partial(functools.reduce, operator.add)
lsub = functools.partial(functools.reduce, operator.sub)
lmul = functools.partial(functools.reduce, operator.mul)
ldiv = functools.partial(functools.reduce, operator.truediv)

b = ldiv([
    ladd([
        5,
        4,
        lsub([
            2,
            lsub([
                3,
                ladd([
                    6,
                    ldiv([
                        4,
                        5
                    ])
                ])
            ])
        ])
    ]),
    lmul([
        3,
        lsub([
            6,
            2
        ]),
        lsub([
            2,
            7
        ])
    ])
])
print(b)

assert a == b
