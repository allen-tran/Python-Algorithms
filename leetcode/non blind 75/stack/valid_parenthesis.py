'''
https://leetcode.com/problems/valid-parentheses/
'''


def isValid(self, s: str) -> bool:
    stack = []

    parenthesis = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in parenthesis:
            top_elem = stack.pop() if stack else '%'
            if top_elem != parenthesis[char]:
                return False

        else:
            stack.append(char)

    return not stack
