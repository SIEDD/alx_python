def multiple_returns(sentence):
    length = len(sentence)
    first_char = sentence[0] if length > 0 else None
    return (length, first_char)

sentence = multiple_returns("Holberton is so cool")
print(sentence)  # Output: (13, 'H')

# sentence_empty = multiple_returns("")
# print(sentence_empty)  # Output: (0, None)

