import itypes


def test_dict_delete():
    orig = itypes.Dict({'a': 1, 'b': 2, 'c': 3})
    new = orig.delete('a')
    assert orig is not new
    assert new == {'b': 2, 'c': 3}


def test_dict_set():
    orig = itypes.Dict({'a': 1, 'b': 2, 'c': 3})
    new = orig.set('d', 4)
    assert orig is not new
    assert new == {'a': 1, 'b': 2, 'c': 3, 'd': 4}


def test_list_delete():
    orig = itypes.List(['a', 'b', 'c'])
    new = orig.delete(1)
    assert orig is not new
    assert new == ['a', 'c']


def test_list_set():
    orig = itypes.List(['a', 'b', 'c'])
    new = orig.set(1, 'xxx')
    assert orig is not new
    assert new == ['a', 'xxx', 'c']
