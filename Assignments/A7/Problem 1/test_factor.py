
import factor as f

def test_factor_fn():
    """Test for factor function in factor.py file"""

    assert f.smallest_factor(1) == 1, "failed on 1"
    assert f.smallest_factor(7) == 7, "failed on a small prime number"
    assert f.smallest_factor(157) == 157, "failed on a large prime number"
    assert f.smallest_factor(6) == 2, "failed on a small non-prime number"
    assert f.smallest_factor(77) == 7, "failed on a large non-prime number"
    assert f.smallest_factor(25) == 5, "failed on a square of a prime"
    assert f.smallest_factor(0) == None, "incorrect input"
