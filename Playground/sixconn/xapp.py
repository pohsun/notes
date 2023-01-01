#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set sw=4 ts=4 fdm=indent fdl=0 fdn=2 ft=python et:

from __future__ import print_function, division
from re import A

import sys

# py2, py3 compatible abc.
# https://stackoverflow.com/a/38668373/2008784
import abc
ABC = abc.ABCMeta('ABC', (object,), {'__slots__': ()})

import threading


class XAppStates(object):
    INIT = "INIT"
    READY = "READY"
    RUN = "RUN"
    TERMINATED = "TERMINATED"
    FAULT = "FAULT"


class XAppFSM(object):
    def __init__(self):
        self._state = XAppStates.INIT

    @property
    def state(self):
        return self._state

    def reset(self):
        if self.state is not XAppStates.TERMINATED or self.state is not XAppStates.FAULT:
            self._state = XAppStates.INIT
        else:
            raise RuntimeError(
                "Bad transition from {} to {}.".format(self.state, XAppStates.TERMINATED))

    def to_ready(self):
        if self.state is XAppStates.INIT:
            self._state = XAppStates.READY
        else:
            raise RuntimeError(
                "Bad transition from {} to {}.".format(self.state, XAppStates.READY))

    def to_run(self):
        if self.state is XAppStates.READY:
            self._state = XAppStates.RUN
        else:
            raise RuntimeError(
                "Bad transition from {} to {}.".format(self.state, XAppStates.RUN))

    def to_terminated(self):
        if self.state is not XAppStates.RUN or self.state is not XAppStates.FAULT:
            self._state = XAppStates.TERMINATED
        else:
            raise RuntimeError(
                "Bad transition from {} to {}.".format(self.state, XAppStates.TERMINATED))

    def to_fault(self):
        self._state = XAppStates.FAULT


class AbsXServerApp(ABC):
    def __init__(self, server):
        self._server = server  # type: socketserver.TCPServer
        self._fsm = XAppFSM()
        self._handleThread = None
        self._handleOutput = None

    def echo(self, args, kwargs):
        return (args, kwargs)

    def setup(self, args, kwargs):
        try:
            self._fsm.to_ready()
            self._handleThread = None
            self._handleOutput = None
            output = self._setup(*args, **kwargs)
            return output
        except:
            self._fsm.to_fault()
            raise

    def _setup(self):
        pass

    def handle(self, args, kwargs):
        def autoexit_handle():
            try:
                self._fsm.to_run()
                self._handle(self._handleOutput, *args, **kwargs)
            except:
                self._fsm.to_fault()
                raise
            else:
                self._fsm.to_terminated()
            finally:
                # As `autoexit_run` is called in a thread, only the thread exits.
                sys.exit()

        try:
            self._handleThread = threading.Thread(
                target=autoexit_handle)
            self._handleThread.start()
        except:
            raise

    @abc.abstractmethod
    def _handle(self, output, *args, **kwargs)
        raise NotImplementedError

    def join(self, timeout=None):
        """ This method returns True just before the run() method starts until just after the run() method terminates. """
        if self._fsm.state is XAppStates.RUN:
            try:
                self._handleThread.join(timeout=timeout)
            except RuntimeError:
                # join() raises a RuntimeError if an attempt is made to join the
                # current thread as that would cause a deadlock. It is also an
                # error to join() a thread before it has been started and attempts
                # to do so raises the same exception.
                pass
            return self._handleThread.is_alive()
        else:
            return False

    def finish(self, args, kwargs):
        if self._fsm.state is XAppStates.TERMINATED:
            try:
                self._finish(*args, **kwargs)
                return self._handleOutput
            except:
                self._fsm.to_fault()
                raise
        elif self._fsm.state is XAppStates.FAULT:
            try:
            finally:
                self._reset()
        else:
            raise RuntimeError(
                "`finish` can be called only when a task is terminated or run into error.")
    
    def _finish(self):
        return 

    def _reset(self):
        self._fsm.reset()


    def shutdown(self):
        threading.Thread(target=self._server.shutdown).start()
