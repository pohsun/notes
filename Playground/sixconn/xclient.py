#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set sw=4 ts=4 fdm=indent fdl=0 fdn=2 ft=python et:

from __future__ import print_function, division

import sys
if sys.version_info[0] == 3:
    import xmlrpc.client as rpcclient
else:
    import xmlrpclib as rpcclient

from . import constants


if __name__ == '__main__':
    cli = rpcclient.ServerProxy(
        "http://{}:{}".format(*constants.TEST_ADDR),
        allow_none=True)
    print(cli.system.listMethods())
    print(cli.echo((None, 1, 2), {"A": 1, "B": 2}))
    print(cli.echo((None, 1, 2), {"A": 1, "B": 2}))
    print(cli.echo((None, 1, 2), {"A": 1, "B": 2}))
    cli.shutdown()
