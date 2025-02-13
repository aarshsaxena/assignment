def three_words(matrix):
    result = [word.upper() for row in words for word in row if len(word) > 3]
    return result

words = [
    ["hi", "hello", "to"],
    ["apple", "go", "code"],
    ["yes", "python", "AI"]
]

result=three_words(words)
print(result)
