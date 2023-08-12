from hello import add, subtract, multiply, division


def test_add():
    assert 2 == add(1, 1)


def test_subtract():
    assert 0 == subtract(1, 1)


def test_multiply():
    assert 6 == multiply(2, 3)


def test_division1():
    assert 2 == division(6, 3)


def test_division2():
    assert None == division(6, 0)
