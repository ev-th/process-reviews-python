class Scrabble:
    def __init__(self, word):
        self.word = word
        self.letter_values = {
            'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1, 'l': 1, 'n': 1, 'r': 1,
            's': 1, 't': 1, 'd': 2, 'g': 3, 'b': 3, 'c': 3, 'm': 3, 'p': 3,
            'f': 4, 'h': 4, 'v': 4, 'w': 4, 'y': 4, 'k': 5, 'j': 8, 'x': 8,
            'q': 10, 'z': 10
        }

    def score(self):
        return sum(
            [self.letter_values.get(char.lower(), 0) for char in self.word]
        )