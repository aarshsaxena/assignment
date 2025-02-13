def comprehension_matrix(matrix):
    result = [num ** 2 for row in matrix for num in row if num % 2 == 0]
    return result

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result=comprehension_matrix(matrix)
print(result)
