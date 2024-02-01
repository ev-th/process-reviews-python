from lib.is_leap_year import is_leap_year

def get_leap_year_range(start_year: int, end_year: int) -> [int]:
    return [year for year in range(start_year, end_year + 1) if is_leap_year(year)]