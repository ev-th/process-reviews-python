def get_middle(word: str) -> str:
    index = len(word) // 2

    if len(word) % 2 == 0:
        return word[index - 1 : index + 1]

    return word[index]