#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set sw=4 ts=4 fdm=indent fdl=0 fdn=2 ft=python et:

from __future__ import print_function, division

import time

from .core.app import AbsApp


class EchoApp(AbsApp):
    def _handle(self, *args, **kwargs):
        return (args, kwargs)

    @AbsApp.dec_post_finish_shutdown
    def _finish_success(self):
        pass

    @AbsApp.dec_post_finish_reset
    def _finish_exception(self):
        pass


class SleepApp(AbsApp):
    def _handle(self, secs):
        time.sleep(secs)
        return secs

    @AbsApp.dec_post_finish_shutdown
    def _finish_success(self):
        pass

    @AbsApp.dec_post_finish_reset
    def _finish_exception(self):
        pass
