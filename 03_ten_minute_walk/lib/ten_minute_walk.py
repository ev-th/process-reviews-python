from collections import Counter

def ten_minute_walk(directions: [str]) -> bool:
    if len(directions) != 10:
        return False

    counter = Counter(directions)

    if counter['n'] == counter['s'] and counter['w'] == counter['e']:
        return True

    return False
