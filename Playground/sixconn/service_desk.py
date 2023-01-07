#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set sw=4 ts=4 fdm=indent fdl=0 fdn=2 ft=python et:

from __future__ import print_function, division


from .core.app import AbsApp


class ServiceDesk(AbsApp):
    def __init__(self, server):
        super().__init__(server)
        self
