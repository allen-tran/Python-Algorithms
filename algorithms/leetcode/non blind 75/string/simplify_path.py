'''
https://leetcode.com/problems/simplify-path/
'''

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        temp = path.split('/')
        
        for i in temp:
            if i == '..':
                if stack:
                    stack.pop()
            elif i == '.' or not i:
                continue
            else:
                stack.append(i)
                
        final_str = "/" + "/".join(stack)
        return final_str
