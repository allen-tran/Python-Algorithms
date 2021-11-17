'''
https://leetcode.com/problems/find-the-celebrity/
'''


def knows(i, j):
    return True


class Solution:
    def findCelebrity(self, n):
        # consider everyone to be a celebrity and continiously call knows
        # to find out wether this person should be a celeb or not
        self.n = n
        celebrity = 0

        for i in range(1, n):
            if knows(celebrity, i):
                celebrity = i
        if self.is_celebrity(celebrity):
            return celebrity
        return -1

    def is_celebrity(self, i):
        for j in range(self.n):
            if i == j:
                continue

            if knows(i, j) or not knows(j, i):
                return False
        return True
