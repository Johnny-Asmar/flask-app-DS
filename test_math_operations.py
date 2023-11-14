
# File: test_math_operations.py
 
def add(x, y):

    return x + y
 
def subtract(x, y):

    return x - y
 
def test_addition():

    assert add(2, 3) == 5

    assert add(0, 0) == 0

    assert add(-1, 1) == 0
 
def test_subtraction():

    assert subtract(5, 3) == 2

    assert subtract(0, 0) == 0

    assert subtract(-1, -1) == 0

