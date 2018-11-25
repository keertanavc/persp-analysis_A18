import operations as op
import pytest

def test_operations():
    """Test for operate function in operations.py file"""

    with pytest.raises(TypeError) as excinfo:
        op.operate(6, 8, 10)
    assert excinfo.value.args[0] == "oper must be a string"
    assert op.operate(1, 5, '+') == 6, "fails for addition"
    assert op.operate(6, 10, '-') == -4, "fails for subtraction"
    assert op.operate(7, 8, '*') == 56, "fails for multiplication"
    assert op.operate(6, 4, '/') == 1.5, "fails for division"
    with pytest.raises(ZeroDivisionError) as excinfo:
        op.operate(6, 0, '/')
    assert excinfo.value.args[0] == "division by zero is undefined"
    with pytest.raises(ValueError) as excinfo:
        op.operate(6, 0, 'foo')
    assert excinfo.value.args[0] == "oper must be one of '+', '-', '/', or '*'"
