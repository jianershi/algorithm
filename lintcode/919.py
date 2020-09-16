"""
919. Meeting Rooms II
https://www.lintcode.com/problem/meeting-rooms-ii/description?_from=ladder&&fromId=106
sweeping line
九章强化班
"""
"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Datatype:
    START = 1
    END = 0

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        # Write your code here
        list = [] #timestamp, event
        for interval in intervals:
            list.append((interval.start, Datatype.START))
            list.append((interval.end, Datatype.END))
        list.sort()

        max_required = 0
        count = 0
        for _, event in list:
            if event == Datatype.START:
                count += 1
            else:
                count -= 1
            max_required = max(max_required, count)
        return max_required
