import month_len as ml

def test_month_len():
    """Test for month_length function in month_len.py file"""

    assert ml.month_length("June") == 30, "fails for months with 30 days"
    assert ml.month_length("August") == 31, "fails for months with 31 days"
    assert ml.month_length("February") == 28, "fails for a normal February"
    assert ml.month_length("February", True) == 29, "fails for a leap year normal February"
    assert ml.month_length("Foo") == None, "fails for an invalid month"
