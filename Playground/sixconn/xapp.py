#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set sw=4 ts=4 fdm=indent fdl=0 fdn=2 ft=python et:

from __future__ import print_function, division

import sys
if sys.version_info[0] == 3:
    import xmlrpc.server as rpcserver
    import xmlrpc.client as rpcclient
else:
    import SimpleXMLRPCServer as rpcserver
    import xmlrpclib as rpcclient

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
        self._server = server
        self._counter = 0

    def echo(self, args, kwargs):
        self._counter += 1
        print(self._counter)
        return (args, kwargs)

    def poll(self):
        pass

    def shutdown(self):
        threading.Thread(target=server.shutdown).start()


if __name__ == '__main__':
    server = rpcserver.SimpleXMLRPCServer(
            ("127.0.0.1", 54321),
            allow_none=True)
    app = AbsXServerApp(server)
    server.register_instance(app)

    server.register_introspection_functions()
    t = threading.Thread(target=server.serve_forever)
    t.start()

    cli = rpcclient.ServerProxy(
        "http://{}:{}".format(*server.server_address),
        allow_none=True)
    print(cli.system.listMethods())
    print(cli.echo((None, 1, 2), {"A": 1, "B": 2}))
    print(cli.echo((None, 1, 2), {"A": 1, "B": 2}))
    print(cli.echo((None, 1, 2), {"A": 1, "B": 2}))
    cli.shutdown()
