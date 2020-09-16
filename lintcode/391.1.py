"""
391. Number of Airplanes in the Sky
https://www.lintcode.com/problem/number-of-airplanes-in-the-sky/description
九章强化班。扫描线sweep line
"""
"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import sys
class Event:
    TAKEOFF = 1
    LANDING = 0
class Solution:
    """
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """
    def countOfAirplanes(self, airplanes):
        if not airplanes:
            return 0

        list = []
        for interval in airplanes:
            list.append((interval.start, Event.TAKEOFF))
            list.append((interval.end, Event.LANDING))

        list.sort()

        count = 0
        max_count = -sys.maxsize

        for time, event in list:
            if event == Event.TAKEOFF:
                count += 1
            else:
                count -= 1
            max_count = max(max_count, count)

        return max_count
