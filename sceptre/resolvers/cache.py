from sceptre.resolvers import Resolver
"""
sceptre.resolvers.cache

This module implements a singleton ResolverCache that is used
to store the state for resolved values. Sceptre will first attempt
to call the cache to retrieve a resolver value before triggering
the resolver call.
"""


class ResolverCache(object):
    class __ResolverCache:

        def __init__(self):
            self.cache = {}
            self.STATES = {
                "RESOLVING": "resolving",
                "RESOLVED": "resolved"
            }

        @staticmethod
        def add(self, stack, prop, key, value):
            self.cache.update(
                "{}.{}".format(stack, prop),
                {
                    "key": key,
                    "value": value,
                    "state": self._get_state(value)
                }
            )

        @staticmethod
        def update(self):
            pass

        def _get_state(self, value):
            if value is isinstance(Resolver):
                return self.STATES.RESOLVING
            return self.STATES.RESOLVED

    instance = None

    def __new__(cls):
        if not ResolverCache.instance:
            ResolverCache.instance = ResolverCache.__ResolverCache()
        return ResolverCache.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name):
        return setattr(self.instance, name)
