"""
42. Trapping Rain Water
https://leetcode.com/problems/trapping-rain-water/submissions/
prefix
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_from_left = self.findMax(height)
        max_from_right = self.findMax(height[::-1])[::-1]
        
        area = 0
        for i in range(n):
            area += max(0, min(max_from_left[i], max_from_right[i]) - height[i])
            
        return area
    
    def findMax(self, height):
        res = []
        nowMax = -1
        for h in height:
            if h > nowMax:
                nowMax = h
            res.append(nowMax)
        return res
