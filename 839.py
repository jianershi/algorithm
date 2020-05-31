"""
思路：
如果都第一个数排序完成了，剩下的跟https://www.lintcode.com/problem/merge-intervals/description一个思路。
可以先排序，然后再处理。O(nlogn+n)
也可一旦决定现在的顺序了立马就处理（n）。自己排序的话只需要花O(n)的时间
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
    @param list1: one of the given list
    @param list2: another list
    @return: the new sorted list of interval
    """
    def mergeTwoInterval(self, list1, list2):
        # write your code here
        intervals = []
        i, j = 0, 0
        while i < len(list1) and j < len(list2):
            if list1[i].start < list2[j].start:
                self.push_back(list1[i], intervals)
                i += 1
            else:
                self.push_back(list2[j], intervals)
                j += 1

        while i < len(list1):
            self.push_back(list1[i], intervals)
            i += 1
        while j < len(list2):
            self.push_back(list2[j], intervals)
            j += 1

        return intervals
    def push_back(self, interval, intervals):
        if not intervals:
            intervals.append(interval)
            return
        last = intervals[-1]
        if interval.start > last.end:
                intervals.append(interval)
        else:
            last.end = max(last.end, interval.end)
        
