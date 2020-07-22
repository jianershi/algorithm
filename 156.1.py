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
        result = []
        intervals.sort(key = lambda x: (x.start, x.end))
        for interval in intervals:
            if not result:
                result.append(interval)
                continue
            last = result[-1]
            if last.end < interval.start:
                result.append(interval)
            else:
                result[-1].end = max(last.end, interval.end)
            
        return result