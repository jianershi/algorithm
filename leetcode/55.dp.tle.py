"""
55. Jump Game
https://leetcode.com/problems/jump-game/
dp.
o(n^2) tle
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[0] = True

        for j in range(n):
            for i in range(j):
                if dp[i] and nums[i] + i >= j:
                    dp[j] = True
                    break
        return dp[n - 1]