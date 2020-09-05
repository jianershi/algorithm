"""
355. shuttleInBuildings
https://www.lintcode.com/problem/shuttleinbuildings/description?_from=contest&&fromId=103
dp          
"""
from collections import deque
class Solution:
    """
    @param heights: the heights of buildings.
    @param k: the vision.
    @param x: the energy to spend of the first action.
    @param y: the energy to spend of the second action.
    @return: the minimal energy to spend.
    """
    def shuttleInBuildings(self, heights, k, x, y):
        # write your code here.
        stack = []
        n = len(heights)
        first_highest = [-1] * n
        for i in range(n):
            while stack and heights[stack[-1]] < heights[i]:
                idx = stack.pop()
                if i - idx <= k:
                    first_highest[i] = idx
            stack.append(i)
        dp = [sys.maxsize] * (n)
        
        dp[0] = 0
        
        for i in range(1,n):
            dp[i] = min(dp[i],dp[i - 1] + y)
            if i >= 2:
                dp[i] = min(dp[i],dp[i - 2] + y)
            if first_highest[i] != -1:
                dp[i] = min(dp[i],dp[first_highest[i]] + x)
        
        return dp[n-1]