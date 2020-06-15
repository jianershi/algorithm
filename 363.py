"""
363. Trapping Rain Water
https://www.lintcode.com/problem/trapping-rain-water/description?_from=ladder&&fromId=106
monotonous stack (decreasing)

don't have to flush the stack. because if it is a decreasing stack, anything that is still remaining
on the stack will be decreasing as well, which means, no water can hold to the right side of it.
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
                left = heights[stack[-1]] if stack else heights[top] #cannot hold water for the 1st item
                left_index = stack[-1] if stack else -1 #easier to calculate length
                length = (i - left_index - 1)
                if left < curr:
                    water_capacity += (left - heights[top]) * length
                else:
                    water_capacity += (curr - heights[top]) * length
            stack.append(i)

        return (water_capacity)
