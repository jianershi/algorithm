"""
383. Container With Most Water
https://www.lintcode.com/problem/container-with-most-water/description?_from=ladder&&fromId=131
11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/submissions/
"""
class Solution:
    """
    @param heights: a vector of integers
    @return: an integer
    """
    def maxArea(self, heights):
        if not heights:
            return 0
        n = len(heights)
        l, r = 0, n - 1
        max_area = 0
        while l < r:
            if heights[l] <= heights[r]:
                max_area = max(max_area, (r - l) * heights[l])
                l += 1
            else: 
                max_area = max(max_area, (r - l) * heights[r])
                r -= 1
                
        return max_area