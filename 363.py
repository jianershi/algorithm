"""
363. Trapping Rain Water
https://www.lintcode.com/problem/trapping-rain-water/description?_from=ladder&&fromId=106
monotonous stack (decreasing)
"""
import sys
class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """
    def trapRainWater(self, heights):
        # write your code here
        stack = []
        water_capacity = 0
        n = len(heights)
        for i in range(n):
            curr = heights[i]
            while stack and curr >= heights[stack[-1]]:
                top = stack.pop()
                left = heights[stack[-1]] if stack else heights[top]
                left_index = stack[-1] if stack else -1
                if left < curr:
                    water_capacity += (left - heights[top]) * (i - left_index - 1)
                else:
                    water_capacity += (curr - heights[top]) * (i - left_index - 1)
            stack.append(i)

        return (water_capacity)
