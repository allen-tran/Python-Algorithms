'''
https://leetcode.com/problems/shortest-word-distance/
'''


# def shortestDistance(wordsDict, word1, word2):
#     min_val = 1000
#     l, r = 1000, 1000

#     for i in range(len(wordsDict)):
#         if wordsDict[i] == word1:
#             l = i
#             min_val = min(min_val, abs(r - l))
#         elif wordsDict[i] == word2:
#             r = i
#             min_val = min(min_val, abs(r-l))

#     return min_val


def shortestDistance(wordsDict, word1, word2):
    result = float('inf')
    x, y = None, None

    for i in range(len(wordsDict)):
        if wordsDict[i] == word1:
            x = i
        if wordsDict[i] == word2:
            y = i
        if x is not None and y is not None:
            result = min(result, abs(x-y))
    return result

print(shortestDistance(["practice", "makes", "perfect",
      "coding", "makes"], "coding", "practice"))
