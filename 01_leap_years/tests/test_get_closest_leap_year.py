from lib.get_closest_leap_year import get_closest_leap_year

def test_get_closest_leap_year_when_passed_leap_year_returns_same_year():
    res = get_closest_leap_year(2000)
    assert res == 2000

def test_get_closest_leap_year_when_passed_year_after_leap_year_returns_that_leap_year():
    res = get_closest_leap_year(2001)
    assert res == 2000

def test_get_closest_leap_year_when_passed_two_years_after_leap_year_returns_that_leap_year():
    res = get_closest_leap_year(2002)
    assert res == 2000

def test_get_closest_leap_year_when_passed_year_before_leap_year_returns_that_leap_year():
    res = get_closest_leap_year(2003)
    assert res == 2004

def test_get_closest_leap_year_when_passed_1900_returns_1896():
    res = get_closest_leap_year(1900)
    assert res == 1896

def test_get_closest_leap_year_when_passed_1899_returns_1896():
    res = get_closest_leap_year(1899)
    assert res == 1896