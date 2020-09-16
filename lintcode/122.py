"""
122. Largest Rectangle in Histogram
https://www.lintcode.com/problem/largest-rectangle-in-histogram/description
monotonous stack
"""
class Solution:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """
    def largestRectangleArea(self, height):
        # write your code here
        if not height:
            return 0

        n = len(height)

        stack = []
        max_area = 0
        for i in range(n + 1): # to prepare for -1 incase all the height is increasing
            curr_height = -1 if i == n else height[i]
            while stack and curr_height <= height[stack[-1]]:
                h = height[stack.pop()]
                left = 0 if len(stack) == 0 else stack[-1] + 1
                right = i - 1
                area = (right - left + 1) * h
                max_area = max(max_area, area)

            stack.append(i)

        return max_area
