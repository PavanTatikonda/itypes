# itypes

Basic immutable container types for Python.

A simple implementation that's designed for simplicity over performance.

Use these in circumstances where it may result in more comprehensible code,
or when you want to create custom types with restricted, immutable interfaces.

For an alternative implementation designed for performance,
please see [pyrsistent](https://github.com/tobgu/pyrsistent).

### Installation

Install using `pip`:

    pip install itypes

### Dictionaries and lists are supported.

    >>> import itypes
    >>> d = itypes.Dict({'a': 1, 'b': 2, 'c': 3})
    >>> l = itypes.List(['a', 'b', 'c'])

### On instantiation, nested types are coerced to immutables.

    >>> d = itypes.Dict({'a': 123, 'b': ['a', 'b', 'c']})
    >>> d['b']
    List(['a', 'b', 'c'])

### Assignments and deletions return new copies.

Methods: `set(key, value)`, `delete(key)`

    >>> d2 = d.set('c', 456)
    >>> d2
    Dict({'a': 123, 'b': ['a', 'b', 'c'], 'c': 456})
    >>> d3 = d2.delete('a')
    >>> d3
    Dict({'b': ['a', 'b', 'c'], 'c': 456})

### Standard assignments and deletions fail.

    >>> d['z'] = 123
    TypeError: 'Dict' object doesn't support item assignment
    >>> del(d['c'])
    TypeError: 'Dict' object doesn't support item deletion

### Nested lookups.

Method: `get_in(keys, default=None)`

    >>> d['b'][-1]
    'c'
    >>> d['b'][5]
    IndexError: list index out of range
    >>> d.get_in(['b', -1])
    'c'
    >>> d.get_in(['b', 4])
    None

### Nested assignments and deletions.

Methods: `set_in(keys, value)`, `delete_in(keys)`

    >>> d2 = d.set_in(['b', 1], 'xxx')
    >>> d2
    Dict({'a': 123, 'b': ['a', 'xxx', 'c']})
    >>> d3 = d2.delete_in(['b', 0])
    >>> d3
    Dict({'a': 123, 'b': ['xxx', 'c']})

### Equality works against standard types.

    >>> d = itypes.Dict({'a': 1, 'b': 2, 'c': 3})
    >>> d == {'a': 1, 'b': 2, 'c': 3}
    True

### Objects are hashable.

    >>> hash(d)
    277752239

### Shortcuts for switching between mutable and immutable types.

Functions: `to_mutable(instance)`, `to_immutable(value)`

    >>> value = itypes.to_mutable(d)
    >>> value
    {'a': 123, 'b': ['a', 'b', 'c']}
    >>> itypes.to_immutable(value)
    Dict({'a': 123, 'b': ['a', 'b', 'c']})

### Subclassing.

Only private attribute names may be set on instances. Use `@property` for attribute access.

Define a `.clone(self, data)` method if objects have additional state.

Example:

    class Configuration(itypes.Dict):
        def __init__(self, title, *args, **kwargs):
            self._title = title
            super(Configuration, self).__init__(*args, **kwargs)

        @property
        def title(self):
            return self._title

        def clone(self, data):
            return Configuration(self._title, data)

Using the custom class:

    >>> config = Configuration('worker-process', {'hostname': 'example.com', 'dynos': 4})
    >>> config.title
    'worker-process'
    >>> new = config.set('dynos', 2)
    >>> new
    Configuration({'dynos': 2, 'hostname': 'example.com'})
    >>> new.title
    'worker-process'
