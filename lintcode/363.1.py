"""
363. Trapping Rain Water
https://www.lintcode.com/problem/trapping-rain-water/description?_from=ladder&&fromId=106

min(max_left, max_right) - own height
"""
import sys
class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """
    def trapRainWater(self, heights):
        # write your code here
        max_left = self.calculate_max_left(heights)
        max_right = self.calculate_max_left(heights[::-1])[::-1]

        water_capacity = 0
        for i in range(len(heights)):
            water_capacity += max(0, min(max_left[i], max_right[i]) - heights[i])

        return water_capacity

    def calculate_max_left(self, heights):
        results = []
        max_so_far = -sys.maxsize
        for h in heights:
            if h > max_so_far:
                max_so_far = h
            results.append(max_so_far)
        return results
