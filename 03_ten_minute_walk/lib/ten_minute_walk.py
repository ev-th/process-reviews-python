from collections import Counter

def ten_minute_walk(directions: [str]) -> bool:
    counter = Counter(directions)

    return all([
        len(directions) == 10,
        counter['n'] == counter['s'],
        counter['w'] == counter['e'],
    ])

