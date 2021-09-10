def border(mat):
    l, r = 0, len(mat)-1
    res = []
    while l < r:
        t, b = l, r

        for i in range(left, r-1):
            res.append(mat[t][i])

