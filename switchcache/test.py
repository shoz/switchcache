# -*- coding: utf-8 -*-

from nose.tools import raises
from switchcache import *
from switchcache import NotConfiguredYet
import memcache

class Configure:
    HOSTS = ['127.0.0.1:11211']
    CACHE = {
        'foo': 'bar',
        'fuga': 'hoge'
    }
mc = memcache.Client(Configure.HOSTS)

class TestNotConfigured:
    @raises(NotConfiguredYet)
    def test_no_cache_with_not_configured(self):
        no_cache(None)
        
    @raises(NotConfiguredYet)
    def test_with_cache_with_not_configured(self):
        with_cache(None)

    @raises(NotConfiguredYet)
    def test_with_clause_not_configuerd(self):
        with cache:
            pass

class TestConfigured:
    def setup(self):
        init(Configure)
        @with_cache
        def test_with_cache(s):
            for k, v in Configure.CACHE.items():
                assert mc.get(k) == v
            return s
        @no_cache
        def test_no_cache(s):
            for k, v in Configure.CACHE.items():
                assert mc.get(k) == None
            return s
        self.test_with_cache = test_with_cache
        self.test_no_cache = test_no_cache
    def test_with_cache_entity(self):
        assert self.test_with_cache('test') == 'test'
    def test_no_cache_entity(self):
        assert self.test_no_cache('test') == 'test'
    def test_with_clause(self):
        with cache:
            for k, v in Configure.CACHE.items():
                assert mc.get(k) == v
        for k, v in Configure.CACHE.items():
            assert mc.get(k) == None
    def teardown(self):
        init(None)
