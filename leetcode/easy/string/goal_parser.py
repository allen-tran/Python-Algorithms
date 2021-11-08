'''
https://leetcode.com/problems/goal-parser-interpretation/
'''


def interpret(self, command):
    return command.replace('()', 'o').replace('(al)', 'al')
