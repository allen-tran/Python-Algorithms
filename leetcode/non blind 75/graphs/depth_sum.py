from typing import Collection

"""
https://leetcode.com/problems/nested-list-weight-sum/
"""

"""
dfs solution:
"""


class Solution:
    def depthSum(self, nestedList):
        return self.dfs(nestedList, 1)

    """
    depth first search
    take in the list but then also take in the depth
    """

    def dfs(self, nested_list, depth):
        total = 0
        # for loop that goes through the nested lsit
        for i in nested_list:
            # if is is an intger, meaning it isnt a bracket
            if i.isInteger():
                total += i.getInteger() * depth
            # but then if we see a bracket, we can just increment the deptj
            else:
                total += self.dfs(i.getList(), depth + 1)
        return total


"""
bfs solution:
def depthSum(nestedList):
    q = Collection.deque(nestedList)
    depth = 1
    total = 0
    while q:
        for i in range(len(q)):
            nested = q.pop()
            if nested.isInteger():
                total += nested.getInteger() * depth

            else:
                q.extendleft(nested.getList())
        depth += 1
    return total
"""
