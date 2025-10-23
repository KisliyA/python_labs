def _verify_row_lengths(mat: list[list[float | int]]) -> bool:
    rowl = len(mat[0])
    for row in mat:
        if len(row) != rowl:
            return False
    return True

def transpose(matrix: list[list[float | int]]) -> list[list[float | int]] | str:
    if not matrix:
        return []
    if not _verify_row_lengths(matrix):
        return "ValueError"
    return [[matrix[row][col] for row in range(len(matrix))] 
            for col in range(len(matrix[0]))]

def row_sums(mat: list[list[float | int]]) -> list[float]:
    if not _verify_row_lengths(mat):
        return "ValueError"
    return [sum(i) for i in mat]


def col_sums(mat: list[list[float | int]]) -> list[float]:
    if not _verify_row_lengths(mat):
        return "ValueError"
    return row_sums(transpose(mat))

print(transpose([[1, 2], [3, 4]]))  # [[1, 3], [2, 4]]
print(transpose([[1], [2], [3]]))    # [[1, 2, 3]]
print(transpose([[1, 2], [3, 4]]))   # [[1, 3], [2, 4]]
print(transpose([]))                 # []
print(transpose([[1, 2], [3]]))      # ValueError

print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))

print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))

