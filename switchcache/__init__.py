# -*- coding: utf-8 -*-

__all__ = ['init', 'with_cache', 'no_cache', 'cache', 'times', 'twice']

import functools
import memcache

_config = {'obj': None}

class NotConfiguredYet(Exception):
    pass
_msg = 'Call switchcache.init() before using with_cache/no_cache/cache'

def init(obj):
    _config['obj'] = obj

def with_cache(testfunc):
    if _config['obj'] == None:
        raise NotConfiguredYet(_msg)
    @functools.wraps(testfunc)
    def wrapper(*args, **kwargs):
        _build_cache(_config['obj'])
        result = testfunc(*args, **kwargs)
        _clear_cache(_config['obj'])
        return result
    return wrapper

def no_cache(testfunc):
    if _config['obj'] == None:
        raise NotConfiguredYet(_msg)
    _clear_cache(_config['obj'])
    return testfunc

def _build_cache(config_obj):
    mc = memcache.Client(config_obj.HOSTS)
    for key, value in config_obj.CACHE.items():
        mc.set(key, value)

def _clear_cache(config_obj):
    mc = memcache.Client(config_obj.HOSTS)
    mc.flush_all()

class Cache():
    def __enter__(self):
        if _config['obj'] == None:
            raise NotConfiguredYet(_msg)
        _build_cache(_config['obj'])
    def __exit__(self, exc_type, exc_value, traceback):
        _clear_cache(_config['obj'])

cache = Cache()

def times(n):
    def wrapper1(testfunc):
        @functools.wraps(testfunc)
        def wrapper2(*args, **kwargs):
            results = []
            for i in range(n):
                results.append(testfunc(*args, **kwargs))
            return results
        return wrapper2
    return wrapper1

twice = times(2)
