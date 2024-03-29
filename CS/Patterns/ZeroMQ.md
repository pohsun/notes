#CS/Patterns #CS/WebDev 

# What is ZeroMQ

As described in [the zguide][zguide], *ZeroMQ (also known as ØMQ, 0MQ, or zmq) looks like an embeddable networking library but acts like a concurrency framework. It gives you sockets that carry atomic messages across various transports like in-process, inter-process, TCP, and multicast. You can connect sockets N-to-N with patterns like fan-out, pub-sub, task distribution, and request-reply. It’s fast enough to be the fabric for clustered products. Its asynchronous I/O model gives you scalable multicore applications, built as asynchronous message-processing tasks. It has a score of language APIs and runs on most operating systems. ZeroMQ is from [iMatix](http://www.imatix.com/) and is LGPLv3 open source.*

In short, by hiding sockets manipulation routines into specific patterns, ZeroMQ concentrate on communicating between nodes and users could focus on using the messages from peers.

References: 
* [The zguide][zguide]
    * Python users should also pay attention to [this repo](https://github.com/booksbyus/zguide/blob/master/examples/Python)
* [PyZMQ Documentation][pyzmq ]
* [The Architecture of Open Source Applications (Volume 2): ZeroMQ (aosabook.org)](https://www.aosabook.org/en/zeromq.html)

# The Sockets
## REQ
## REP
## STREAM

```embed-python
PATH: vault://CS/Patterns/attachments/zmq_stream.py
```



[zguide]: https://zguide.zeromq.org/
[pyzmq]: https://pyzmq.readthedocs.io/en/latest/


