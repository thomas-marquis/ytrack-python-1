import string


def tokenize(sentence: str) -> list[str]:
    for punct in string.punctuation:
        sentence = sentence.replace(punct, " ")
    
    tokens = sentence.split()
    return [token.lower() for token in tokens]
