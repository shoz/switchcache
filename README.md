switchcache
===

Test utils for testing with memcache

## Preparation

```python
from switchcache import init
class Configure:
    HOSTS = ['127.0.0.1:11211']
    CACHE = {
        'foo': 'bar',
        'fuga': 'hoge'
    }
init(Configure)
```

## Decorators

```python
from switchcache import with_cache, no_cache
@with_cache
def test_with_cache():
    <Cache enabled in this function>
@no_cache
def test_no_cache():
    <Cache disabled in this function>
```


## "With" clause

```python
from switchcache import cache
def test():
    with cache:
       <Cache enabled inside "with">
    <Cache disabled outside "with">
```

### Note

Make sure HOSTS point to a your testing environment.
Your current caches on memcache will be flushed & overrided.

