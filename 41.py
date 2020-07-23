"""
41. Maximum Subarray
https://www.lintcode.com/problem/maximum-subarray/description?_from=ladder&&fromId=37

dp[i] maximum sum of continuous array inlcuding point X[i]

analysis, dp has the choice of either including previous sum or not, either way, it must including X[i] by definition.
dp[i] = dp[i - 1] + X[i] if dp[i - 1] > 0, else, it will only make it smaller, so dp[i]
时间复杂度O(N)
intilization
dp[0] = nums[0]
answer: max(dp)
"""
class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        if not nums:
            return 0
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if dp[i - 1] > 0:
                dp[i] = dp[i - 1] + nums[i]
            else:
                dp[i] = nums[i]
        
        return max(dp)