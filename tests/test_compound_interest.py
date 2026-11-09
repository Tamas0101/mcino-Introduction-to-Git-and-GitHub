from compound_interest import compound_interest


def test_compound_interest_two_years():
    assert compound_interest(1000, 2, 10) == 1210


def test_compound_interest_zero_rate():
    assert compound_interest(1000, 2, 0) == 1000


def test_compound_interest_zero_principal():
    assert compound_interest(0, 5, 10) == 0
