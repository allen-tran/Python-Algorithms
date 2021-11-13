'''
https://leetcode.com/problems/generate-parentheses/submissions/
'''


def generateParenthesis(n):
    '''
    only going to add oen parenthesis if open < n
    only add a closing parenthesis if closed < open
    valid IFF open == closed == n
    '''

    stack = []
    res = []

    def backtrack(open_count, closed_count):
        if open_count == closed_count == n:
            res.append("".join(stack))
            return
        if open_count < n:
            stack.append("(")
            backtrack(open_count+1, closed_count)
            stack.pop()
        if closed_count < open_count:
            stack.append(")")
            backtrack(open_count, closed_count+1)
            stack.pop()

    backtrack(0, 0)
    return res


print(generateParenthesis(3))
