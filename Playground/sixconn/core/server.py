#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set sw=4 ts=4 fdm=indent fdl=0 fdn=2 ft=python et:

from __future__ import print_function, division

import sys
if sys.version_info[0] == 3:
    import xmlrpc.server as rpcserver
else:
    import SimpleXMLRPCServer as rpcserver

import threading

from .. import constants
from ..example_app import EchoApp


def create_server(addr):
    server = rpcserver.SimpleXMLRPCServer(
        addr,
        allow_none=True)
    return server

class ThreadedServer(object):
    def __init__(self, addr):
        self, 

    def run_thread(self, app):
        app.bind_server(self._server)
        self._thread = threading.Thread(target=server.serve_forever)
        self._thread.start()
        return t




if __name__ == '__main__':
    server = create_server(constants.TEST_ADDR)

    app = EchoApp()
    app.bind_server(server)

    server.register_introspection_functions()
    t = threading.Thread(target=server.serve_forever)
    t.start()
