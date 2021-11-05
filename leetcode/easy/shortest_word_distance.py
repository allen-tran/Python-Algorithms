'''
https://leetcode.com/problems/shortest-word-distance/
'''


def shortestDistance(wordsDict, word1, word2):
    min_val = 1000
    l, r = 1000, 1000

    for i in range(len(wordsDict)):
        if wordsDict[i] == word1:
            l = i
            min_val = min(min_val, abs(r - l))
        elif wordsDict[i] == word2:
            r = i
            min_val = min(min_val, abs(r-l))

    return min_val


print(shortestDistance(["practice", "makes", "perfect",
      "coding", "makes"], "coding", "practice"))
