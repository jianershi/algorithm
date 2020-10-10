"""
45. Jump Game II
https://leetcode.com/problems/jump-game-ii/
tle
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [sys.maxsize] * n
        dp[0] = 0
        for i in range(n):
            for j in range(1, nums[i] + 1):
                if i + j < n:
                    dp[i + j] = min(dp[i + j], dp[i] + 1)
        return dp[n - 1]