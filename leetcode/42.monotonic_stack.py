"""
42. Trapping Rain Water
https://leetcode.com/problems/trapping-rain-water/submissions/
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        stack = []
        area = 0
        for i in range(n):
            while stack and height[stack[-1]] <= height[i]:
                top = height[stack.pop()]
                l = height[stack[-1]] if stack else top
                l_idx = stack[-1] if stack else 0
                area += (i - l_idx - 1) * (min(l, height[i]) - top)
            stack.append(i)
        return area