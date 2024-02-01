from lib.is_leap_year import is_leap_year

def get_closest_leap_year(year: int) -> int:
    for i in range(5):
        if is_leap_year(year - i):
            return year - i
        elif is_leap_year(year + i):
            return year + i