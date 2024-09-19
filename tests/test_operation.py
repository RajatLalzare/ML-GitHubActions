from src.math_operations import add,sub

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 4) == 3
    assert add(0, 0) == 0
    assert add(1.5, 2.5) == 4.0
    assert add(1000000000, 2000000000) == 3000000000 

def test_sub():
    assert sub(5, 3) == 2
    assert sub(-1, 4) == -5
    assert sub(0, 0) == 0
    assert sub(2.5, 1.5) == 1.0
    assert sub(2000000000, 1000000000) == 1000000000