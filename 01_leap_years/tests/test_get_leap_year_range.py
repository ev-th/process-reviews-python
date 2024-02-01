from lib.get_leap_year_range import get_leap_year_range

def test_get_leap_year_range_returns_list_of_leap_years_between_two_years_inclusive():
    res = get_leap_year_range(1996, 2004)
    assert res == [1996, 2000, 2004]

def test_get_leap_year_range_returns_list_of_leap_years_between_another_two_years():
    res = get_leap_year_range(1895, 1907)
    assert res == [1896, 1904]
