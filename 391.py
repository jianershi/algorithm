# -*- coding: utf-8 -*-

"""
391. Number of Airplanes in the Sky
查分前缀和
"""
"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
# import sys
# class Interval(object):
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end

import sys
class Solution:
    """
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """
    def countOfAirplanes(self, airplanes):
        # write your code here
        if not airplanes:
            return 0

        min_index = 100000
        max_index = -100000

        for interval in airplanes:
            min_index = min(min_index, interval.start)
            max_index = max(max_index, interval.end)


        array = [0] * (max_index - min_index + 1)

        for interval in airplanes:
            array[interval.start - min_index] += 1
            array[interval.end - min_index] -= 1

        prefix_sum = []
        curr_sum = 0
        for i in range(len(array)):
            curr_sum += array[i]
            prefix_sum.append(curr_sum)

        return max(prefix_sum)

# s = Solution()
# airplanes = [
# Interval(1,10),
# Interval(2,3),
# Interval(5,8),
# Interval(4,7),
# ]
# print(s.countOfAirplanes(airplanes))
