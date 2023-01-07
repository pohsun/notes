#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set sw=4 ts=4 fdm=indent fdl=0 fdn=2 ft=python et:

from __future__ import print_function, division


class AppStates(object):
    INIT = "INIT"
    READY = "READY"
    RUN = "RUN"
    TERMINATED = "TERMINATED"
    FAULT = "FAULT"


class AppFSM(object):
    def __init__(self):
        self._state = AppStates.INIT

    @property
    def state(self):
        return self._state

    def reset(self):
        if self.state is not AppStates.TERMINATED or self.state is not AppStates.FAULT:
            self._state = AppStates.INIT
        else:
            raise RuntimeError(
                "Bad transition from {} to {}.".format(self.state, AppStates.TERMINATED))

    def to_ready(self):
        if self.state is AppStates.INIT or self.state is AppStates.TERMINATED:
            self._state = AppStates.READY
        else:
            raise RuntimeError(
                "Bad transition from {} to {}.".format(self.state, AppStates.READY))

    def to_run(self):
        if self.state is AppStates.READY:
            self._state = AppStates.RUN
        else:
            raise RuntimeError(
                "Bad transition from {} to {}.".format(self.state, AppStates.RUN))

    def to_terminated(self):
        if self.state is not AppStates.RUN or self.state is not AppStates.FAULT:
            self._state = AppStates.TERMINATED
        else:
            raise RuntimeError(
                "Bad transition from {} to {}.".format(self.state, AppStates.TERMINATED))

    def to_fault(self):
        self._state = AppStates.FAULT
