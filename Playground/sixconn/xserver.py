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

from . import constants
from . import xapp


if __name__ == '__main__':
    server = rpcserver.SimpleXMLRPCServer(
            constants.TEST_ADDR,
            allow_none=True)

    app = xapp.AbsXServerApp(server)
    server.register_instance(app)

    server.register_introspection_functions()
    t = threading.Thread(target=server.serve_forever)
    t.start()
