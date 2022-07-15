class Bobina:
    def __init__(self, debug=True):
        self._debug = debug
        self._routes = {}
        self._exception_handler = None
        self._middleware = ...

    def debug(self):
        ...

    def add_middleware(self, *, middleware_cls, **middleware_config):
        ...

    def route(self):
        ...

    def on(self):
        ...

    def off(self):
        ...
