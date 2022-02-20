import time


def totalNQueens(n: int) -> int:
    j_col = set()
    neg_slope = set()  # i= -j + b how to get b?  b = i +j
    pos_slope = set()  # i = j + b how to get b? b = i - j
    ans = [0]

    def dfs(i, depth):
        if(depth == n):
            ans[0] += 1
            return
        for j in range(0, n):
            neg_b = i + j
            pos_b = i - j
            if j in j_col or neg_b in neg_slope or pos_b in pos_slope:
                continue
            j_col.add(j)  # prolly faster way to do this but lz lmao
            neg_slope.add(neg_b)
            pos_slope.add(pos_b)
            dfs(i+1, depth+1)
            j_col.remove(j)
            neg_slope.remove(neg_b)
            pos_slope.remove(pos_b)

    dfs(0, 0)
    return ans[0]


for i in range(1, 100):
    start = time.clock_gettime(0)
    totalNQueens(i)
    end = time.clock_gettime(0)
    print(i, end-start)
