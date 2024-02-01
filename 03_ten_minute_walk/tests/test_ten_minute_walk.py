from lib.ten_minute_walk import ten_minute_walk

def test_ten_minute_walk_returns_false_if_walk_isnt_10_minutes():
    assert ten_minute_walk(['w', 's']) is False

def test_ten_minute_walk_returns_false_if_n_count_not_equal_to_s_count():
    assert ten_minute_walk(['w', 'w', 'w', 'e', 'e', 'e', 'n', 'n', 'n', 's']) is False

def test_ten_minute_walk_returns_false_if_w_count_not_equal_to_e_count():
    assert ten_minute_walk(['w', 'w', 'w', 'e', 'e', 'w', 'n', 'n', 's', 's']) is False