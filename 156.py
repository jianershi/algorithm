"""
156. Merge Intervals
https://www.lintcode.com/problem/merge-intervals/description?_from=ladder&&fromId=37
"""
"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals):
        # write your code here
        intervals = sorted(intervals, key=lambda x: (x.start, x.end))
        
        res = []
        n = len(intervals)
        for i in range(n):
            if not res:
                res.append(intervals[i])
                continue
            last = res[-1]
            if intervals[i].start > last.end:
                res.append(intervals[i])
                continue
            last.end = max(intervals[i].end, last.end)
        return res