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


class Server(object):
    def __init__(self, addr, app_cls):
        self._server = rpcserver.SimpleXMLRPCServer(
            constants.TEST_ADDR,
            allow_none=True)
        
        self._app = 
    


if __name__ == '__main__':
    server = rpcserver.SimpleXMLRPCServer(

    app = EchoApp(server)
    server.register_function(app.setup)
    server.register_function(app.handle)
    server.register_function(app.finish)
    server.register_function(app.system_shutdown)
    server.register_function(app.system_echo)
    if constants.DEVMODE:
        server.register_function(app._system_get_state)
        server.register_function(app._system_get_handleOutput)
        server.register_function(app._system_get_traceback)

    server.register_introspection_functions()
    t = threading.Thread(target=server.serve_forever)
    t.start()
