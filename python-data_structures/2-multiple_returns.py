def multiple_returns(sentence):
    length = len(sentence)
    first_char = sentence[0] if length > 0 else None
    return (length, first_char)

sentence = multiple_returns("Holberton is so cool")
sentence_empty = multiple_returns("")


