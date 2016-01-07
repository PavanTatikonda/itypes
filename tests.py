import itypes
import pytest


# [], .get()

def test_dict_get():
    orig = itypes.Dict({'a': 1, 'b': 2, 'c': 3})
    assert orig.get('a') == 1
    assert orig.get('z') is None


def test_dict_lookup():
    orig = itypes.Dict({'a': 1, 'b': 2, 'c': 3})
    assert orig['a'] == 1
    with pytest.raises(KeyError):
        orig['zzz']


def test_list_lookup():
    orig = itypes.List(['a', 'b', 'c'])
    assert orig[1] == 'b'
    with pytest.raises(IndexError):
        orig[999]


# .delete(), .set()

def test_dict_delete():
    orig = itypes.Dict({'a': 1, 'b': 2, 'c': 3})
    new = orig.delete('a')
    assert new == {'b': 2, 'c': 3}


def test_dict_set():
    orig = itypes.Dict({'a': 1, 'b': 2, 'c': 3})
    new = orig.set('d', 4)
    assert new == {'a': 1, 'b': 2, 'c': 3, 'd': 4}


def test_list_delete():
    orig = itypes.List(['a', 'b', 'c'])
    new = orig.delete(1)
    assert new == ['a', 'c']


def test_list_set():
    orig = itypes.List(['a', 'b', 'c'])
    new = orig.set(1, 'xxx')
    assert new == ['a', 'xxx', 'c']


# .get_in()

def test_get_in():
    orig = itypes.Dict({'a': ['x', 'y', 'z'], 'b': 2, 'c': 3})
    assert orig.get_in(['a', -1]) == 'z'
    assert orig.get_in(['dummy', -1]) is None
    assert orig.get_in(['a', 999]) is None


# .delete_in(), .set_in()

def test_delete_in():
    orig = itypes.Dict({'a': ['x', 'y', 'z'], 'b': 2, 'c': 3})
    new = orig.delete_in(['a', 1])
    assert new == {'a': ['x', 'z'], 'b': 2, 'c': 3}

    orig = itypes.Dict({'a': ['x', 'y', 'z'], 'b': 2, 'c': 3})
    new = orig.delete_in(['a'])
    assert new == {'b': 2, 'c': 3}

    orig = itypes.Dict({'a': ['x', 'y', 'z'], 'b': 2, 'c': 3})
    new = orig.delete_in([])
    assert new is None


def test_set_in():
    orig = itypes.Dict({'a': ['x', 'y', 'z'], 'b': 2, 'c': 3})
    new = orig.set_in(['a', 1], 'yyy')
    assert new == {'a': ['x', 'yyy', 'z'], 'b': 2, 'c': 3}

    orig = itypes.Dict({'a': ['x', 'y', 'z'], 'b': 2, 'c': 3})
    new = orig.set_in(['a'], 'yyy')
    assert new == {'a': 'yyy', 'b': 2, 'c': 3}

    orig = itypes.Dict({'a': ['x', 'y', 'z'], 'b': 2, 'c': 3})
    new = orig.set_in([], 'yyy')
    assert new == 'yyy'


# Objects

def test_setting_object_property():
    class Example(itypes.Object):
        pass

    example = Example()
    with pytest.raises(TypeError):
        example.a = 123
