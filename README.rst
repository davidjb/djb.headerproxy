.. contents::

Introduction
============

Simple package that extends the proxy object within ``Paste`` to allow
the WSGI proxy to read its connection location from arbitrary headers.
It will keep all other headers (including ``Host:`` intact during transit);
you may or may not need to adjust what you're doing upstream accordingly.

Configuration
-------------

By default, the proxy will read the host to connect to from the
``X-Proxy-Force-Host`` header and read the connection scheme from
``X-Proxy-Force-Scheme``.  

You can override these using relevant configuration
like follows. Keep in mind that at time of proxy, we're reading headers from
the ``environ`` dictionary, so specify your headers in this manner.  For 
instance, ``X-Proxy-Foobar`` will become visible in the ``environ`` dict
as ``HTTP_PROXY_FOOBAR`` (noting dashes to underscores, and replacement
of ``X`` with ``HTTP``).  You can make this mapping happen thusly::

    [app:proxy]
    use = egg:djb.headerproxy
    force_host = HTTP_PROXY_FORCE_HOST
    force_scheme = HTTP_PROXY_FORCE_SCHEME

The above example is overly verbose, however, as we already default to 
using these specific headers. This does demonstrate how you can customise
this behaviour to suit you -- for instance, if your front-end automatically
provides some headers, you can configure the mapping accordingly.

Warning
-------

If unprotected, this WSGI middleware could be used as an open proxy since
headers can easily be spoofed. You should take steps to either firewall off
your application, drop headers at an upstream web server, run this as a
local socket, or do something similar (or all of the above!).

You've been warned.

Source code
-----------

Available on GitHub at http://github.com/davidjb/djb.headerproxy/ - fork away!

