"""
41. Maximum Subarray
https://www.lintcode.com/problem/maximum-subarray/description?_from=ladder&&fromId=37

dp[i] largest sum of continguous subarray ending in i

dp[i] = max(dp[i - 1] + nums[i - 1], nums[i])

ans: max(dp[i])

intilaization
dp[i] = i

o(n)

"""
import sys
class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        if not nums:
            return 0
        n = len(nums)
        
        dp = []
        for num in nums:
            dp.append(num)
            
        for i in range(n):
            if i == 0:
                dp[i] = nums[i]
                continue
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        
        return max(dp)