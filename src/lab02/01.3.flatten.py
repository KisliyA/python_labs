def flatten(mat: list[list | tuple]) -> list:
    rez = list()
    for i in range(len(mat)):
        if isinstance(mat[i], list) or isinstance(mat[i], tuple):
            for k in mat[i]:
                rez.append(k)
        else:
            return 'TypeError'
    return rez
print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1],[], [2, 3]]))
print(flatten([[1, 2], 'ab']))
