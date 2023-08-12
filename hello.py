def add(x, y):
    """This is an add function"""

    return x + y


def subtract(x, y):
    """This is an subtract function"""
    return x - y


def multiply(x, y):
    """This is an multiplication function"""
    return x * y


def division(x, y):
    """This is an division function"""
    if y == 0:
        return None
    else:
        return x / y


print(add(1, 1))
print(subtract(1, 1))
print(multiply(2, 3))
