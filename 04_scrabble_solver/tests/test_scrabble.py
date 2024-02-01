from lib.scrabble import Scrabble

def test_scrabble_scores_0_with_empty_string():
    scrabble = Scrabble('')
    assert scrabble.score() == 0

def test_scrabble_gives_a_score_of_1():
    scrabble = Scrabble('a')
    assert scrabble.score() == 1

def test_scrabble_gives_f_score_of_4():
    scrabble = Scrabble('f')
    assert scrabble.score() == 4

def test_scrabble_gives_street_score_of_6():
    scrabble = Scrabble('street')
    assert scrabble.score() == 6

def test_scrabble_gives_quirky_score_of_22():
    scrabble = Scrabble('quirky')
    assert scrabble.score() == 22

def test_scrabble_gives_OXYPHENBUTAZONE_score_of_22():
    scrabble = Scrabble('OXYPHENBUTAZONE')
    assert scrabble.score() == 41

def test_scrabble_gives_whitespace_chracters_score_of_0():
    scrabble = Scrabble('\t\n')
    assert scrabble.score() == 0
