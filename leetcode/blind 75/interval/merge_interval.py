'''
https://leetcode.com/problems/merge-intervals/
'''


def merge(intervals):
    if len(intervals) < 2:
        return intervals

    intervals.sort(key=lambda x: x[0])
    merged = []
    merged.append(intervals[0])

    for start, end in intervals[1:]:
        last_end = merged[-1][1]

        if start <= last_end:
            merged[-1][1] = max(end, last_end)
        else:
            merged.append([start, end])
    return merged
