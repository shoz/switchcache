switchcache
===

Test utils for testing with memcache

## with_cache/no_cache decorators

```python
from switchcache import init, with_cache, no_cache

class Configure:
    HOSTS = ['127.0.0.1:11211']
    CACHE = {
        'foo': 'bar',
        'fuga': 'hoge'
    }
init(Configure)

@with_cache
def test_with_cache():
    <Cache enabled in this function>
    
@no_cache
def test_no_cache():
    <Cache disabled in this function>
```

## "with" clause

```python
from switchcache import cache
def test():
    with cache:
       <Cache enabled inside "with">
    <Cache disabled outside "with">
```

## twice/times decorators

```python
from switchcache import twice, times

@twice
def test_twice(s):
    return s
>>> test_twice('foo')
['foo', 'foo']

    
@times(5)
def test_5_times(s):
    return s
>>> test_5_times('bar')
['bar', 'bar', 'bar', 'bar', 'bar']

```

## Note

Make sure HOSTS point to a your testing environment.
Your current caches on memcache will be flushed & overrided.

