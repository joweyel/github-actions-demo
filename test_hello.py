from hello import add, subtract, multiply


def test_add():
    assert 2 == add(1, 1)

def test_subtract():
    assert 0 == subtract(1, 1)
    
def test_multiply():
    assert 6 == multiply(2, 3)