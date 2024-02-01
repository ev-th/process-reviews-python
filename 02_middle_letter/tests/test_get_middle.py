from lib.get_middle import get_middle

def test_returns_middle_letter_of_string_with_odd_length():
    assert get_middle('testing') == 't'

def test_returns_entire_one_character_string():
    assert get_middle('a') == 'a'

def test_return_middle_two_letters_of_string_of_even_length():
    assert get_middle('middle') == 'dd'