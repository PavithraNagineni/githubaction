from src.math_operations import add,sub

def test_add():
    assert add(2,3) == 5
    assert add(-1,1) == 0
    assert add(3,4) == 7
    
def test_sub():
    assert sub(5,3) == 2
    assert sub(3,7) == -4
    assert sub(3,3) == 0