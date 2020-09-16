"""
821. Time Intersection
https://www.lintcode.com/problem/time-intersection/description?_from=ladder&&fromId=106
"""
"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class EventType:
    ONLINE = 1
    OFFLINE = 0

class Solution:
    """
    @param seqA: the list of intervals
    @param seqB: the list of intervals
    @return: the time periods
    """
    def timeIntersection(self, seqA, seqB):
        # Write your code here
        list = []
        for interval in seqA + seqB:
            list.append((interval.start, EventType.ONLINE))
            list.append((interval.end, EventType.OFFLINE))

        list.sort()

        count = 0
        results = []

        range_start = None
        last_count = None
        for i, (timestamp, event) in enumerate(list):
            if event == EventType.ONLINE:
                count += 1
            else:
                count -= 1

            if count == 2:
                if last_count and last_count < 2: #rising edge
                    range_start = timestamp
            elif count < 2:
                if last_count and last_count == 2: #falling edge
                    results.append(Interval(range_start, timestamp))
                    range_start = None
            last_count = count

        return results
