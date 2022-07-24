"""
41. Maximum Subarray
https://www.lintcode.com/problem/maximum-subarray/description?_from=ladder&&fromId=37

prefix sum, then iterate trhough all posibile window
o(n^2)
TLE
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
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]
        
        max_sum = -sys.maxsize
        for i in range(n + 1):
            for j in range(i + 1, n + 1):
                max_sum = max(max_sum, prefix_sum[j] - prefix_sum[i])
                
        return max_sum