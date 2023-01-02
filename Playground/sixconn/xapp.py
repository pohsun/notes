#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set sw=4 ts=4 fdm=indent fdl=0 fdn=2 ft=python et:

from __future__ import print_function, division

import sys
import traceback

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
        if self.state is XAppStates.INIT or self.state is XAppStates.TERMINATED:
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


class AbsXApp(ABC):
    def __init__(self, server):
        self._server = server  # type: ignore
        self._fsm = XAppFSM()
        self._traceback = None
        self._handleThread = None  # type: None | threading.Thread
        self._handleOutput = None

    def _state(self):
        return self._fsm.state

    def setup(self, args=None, kwargs=None):
        args = () if args is None else args
        kwargs = {} if kwargs is None else kwargs
        try:
            self._fsm.to_ready()
            self._handleThread = None
            self._handleOutput = None
            output = self._setup(*args, **kwargs)
            return output
        except:
            self._traceback = sys.exc_info()
            self._fsm.to_fault()
            raise

    def _setup(self):
        pass

    def handle(self, args=None, kwargs=None):
        args = () if args is None else args
        kwargs = {} if kwargs is None else kwargs

        self._handleThread = threading.Thread(
            target=self._handle_worker,
            args=args,
            kwargs=kwargs)
        self._handleThread.start()

    def _handle_worker(self, *args, **kwargs):
        try:
            self._fsm.to_run()
            self._handleOutput = self._handle(*args, **kwargs)
        except:
            self._traceback = traceback.format_exc()
            self._fsm.to_fault()
        else:
            self._fsm.to_terminated()
        finally:
            # As `autoexit_run` is called in a thread, only the thread exits.
            sys.exit()

    @abc.abstractmethod
    def _handle(self, *args, **kwargs):
        return (args, kwargs)

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

    def finish(self, args=None, kwargs=None):
        args = () if args is None else args
        kwargs = {} if kwargs is None else kwargs
        output = {
            XAppStates.TERMINATED: self._handleOutput,
            XAppStates.FAULT: self._traceback
        }
        callback = {
            XAppStates.TERMINATED: self._finish_success,
            XAppStates.FAULT: self._finish_exception
        }

        try:
            return output[self._fsm.state]
        except KeyError:
            raise RuntimeError(
                "`finish` can be called only when a task is terminated or run into error.")
        finally:
            try:
                callback[self._fsm.state](*args, **kwargs)
            except:
                self._traceback = sys.exc_info()
                self._fsm.to_fault()
                raise

    def _finish_success(self):
        """ 
        If you want to close app, call `self.shutdown`.
        If you want to reuse setuped app, call `self._fsm.to_ready`.
        """
        self.shutdown()

    def _finish_exception(self):
        """ 
        If you want to close app, call `self.shutdown`.
        If you want to reuse setuped app, call `self._fsm.to_ready`.
        """
        self._handleThread = None
        self._handleOutput = None
        self._fsm.to_ready()

    def system_echo(self, args=None, kwargs=None):
        args = () if args is None else args
        kwargs = {} if kwargs is None else kwargs
        return (args, kwargs)

    def system_shutdown(self):
        """ Shutdown the serveer. """
        threading.Thread(target=self._server.shutdown).start()


class EchoXServerApp(AbsXApp):
    def _handle(self, *args, **kwargs):
        return (args, kwargs)
