from paste.proxy import TransparentProxy

DEFAULT_MAPPING = {
    'force_host': 'HTTP_X_PROXY_FORCE_HOST',
    'force_scheme': 'HTTP_X_PROXY_FORCE_SCHEME'
}


class HeadersProxy(TransparentProxy):

    def __init__(self, force_host=None,
                 force_scheme='http', header_mapping={}):
        self.header_mapping = header_mapping
        return super(HeadersProxy, self).__init__(force_host, force_scheme)

    def __call__(self, environ, start_response):
        try:
            self.force_host = environ[self.header_mapping['force_host']]
            self.force_scheme = environ[self.header_mapping['force_scheme']]
        except:
            pass

        return super(HeadersProxy, self).__call__(environ, start_response)


def make_header_proxy(global_conf, **kwargs):
    if not kwargs:
        kwargs = DEFAULT_MAPPING
    return HeadersProxy(header_mapping=kwargs)
