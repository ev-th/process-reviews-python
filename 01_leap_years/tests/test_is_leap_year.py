from lib.is_leap_year import is_leap_year

def test_is_leap_year_returns_true_when_divisible_by_400():
    assert is_leap_year(2000) is True

def test_is_leap_year_returns_false_when_divisible_by_100_but_not_400():
    assert is_leap_year(1900) is False

def test_is_leap_year_returns_true_when_divisible_by_4_but_not_100():
    assert is_leap_year(1988) is True

def test_is_leap_year_returns_true_when_not_divisible_by_4():
    assert is_leap_year(1999) is False
