#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set sw=4 ts=4 fdm=indent fdl=0 fdn=2 ft=python et:

from __future__ import print_function, division

import sys
import copy

# py2, py3 compatible abc.
# https://stackoverflow.com/a/38668373/2008784
import abc
ABC = abc.ABCMeta('ABC', (object,), {'__slots__': ()})

import threading


class XAppStates(object):
    INIT = copy.copy(0)
    READY = copy.copy(1)
    RUN = copy.copy(2)
    TERMINATED = copy.copy(3)
    FAULT = copy.copy(-1)


class XAppFSM(object):
    def __init__(self):
        self._state = XAppStates.INIT

    @property
    def state(self):
        return self._state

    def to_ready(self):
        pass

    def to_run(self):
        pass

    def to_terminated(self):
        pass

    def to_fault(self):
        pass
    

class AbsXServerApp(ABC):
    def __init__(self, server):
        self._server = server  # type: socketserver.TCPServer
        self._fsm = XAppFSM()
        self._runThread = None

    def echo(self, args, kwargs):
        return (args, kwargs)

    def setup(self, args, kwargs):
        output = self._setup(*args, **kwargs)
        self._state = 
        return output

    def _setup(self):
        pass

    def run(self, args, kwargs):
        def autoexit_run(*args, **kwargs):
            try:
                self._run(*args, **kwargs)
            finally:
                # As `autoexit_run` is called in a thread, only the thread exits.
                sys.exit()
        self._runT = threading.Thread(
            target=autoexit_run,
            args=args,
            kwargs=kwargs)
        self._runT.start()

    @abc.abstractmethod
    def _run(self, *args, **kwargs)
        raise NotImplementedError

    def join(self, timeout=None):
        """ This method returns True just before the run() method starts until just after the run() method terminates. """
        try:
            self._runT.join(timeout=timeout)
        except RuntimeError:
            # join() raises a RuntimeError if an attempt is made to join the
            # current thread as that would cause a deadlock. It is also an
            # error to join() a thread before it has been started and attempts
            # to do so raises the same exception.
            pass
        return self.is_alive()

    def finish(self, args, kwargs):
        return self._finish(*args, **kwargs)
    
    def _finish(self):
        pass

    def shutdown(self):
        threading.Thread(target=self._server.shutdown).start()