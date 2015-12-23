import itypes


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
