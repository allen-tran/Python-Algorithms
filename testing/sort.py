

def sort_matrices(mat, n):
    setNum = set()

    for i in mat:
        setNum /= sum(i)

    missing_number = (n - setNum).pop()
    for i in mat:
        if "?" in i:
            i[row.index("?")] = missing_number
            break
    return missing_num, mat

def missing_matrices(mat):
    res = []
    n = set("?") | set([i for i in list(range(1, 17))])

    for i, matrix in enumerate(mat):
        num, new_matrix = sort_matrices(matrix, n)
        res.append(num, i)
        mat[i] = matrix
    res.sort()
    return [mat[i] for num, i in res]

print(missing_matrices([["1"],["2"], ["3"]]))