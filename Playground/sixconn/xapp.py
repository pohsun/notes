#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set sw=4 ts=4 fdm=indent fdl=0 fdn=2 ft=python et:

from __future__ import print_function, division

# py2, py3 compatible abc.
# https://stackoverflow.com/a/38668373/2008784
import abc
ABC = abc.ABCMeta('ABC', (object,), {'__slots__': ()})

import threading


class XServerStates(object):
    INIT = 0
    READY = 1
    RUN = 2
    TERMINATED = 3
    FAULT = -1

class AbsXServerApp(ABC):
    def __init__(self, server):
        self._server = server  # type: socketserver.TCPServer

    def echo(self, args, kwargs):
        return (args, kwargs)

    @abc.abstractmethod
    def setup(self):
        pass

    @abc.abstractmethod
    def run()

    def poll(self):
        pass

    def shutdown(self):
        threading.Thread(target=self._server.shutdown).start()
