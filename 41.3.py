"""
41. Maximum Subarray
https://www.lintcode.com/problem/maximum-subarray/description?_from=ladder&&fromId=37

continuously check prefix sum

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
        now_sum = 0
        min_sum = 0
        max_sum = -sys.maxsize
        for num in nums:
            now_sum += num
            max_sum = max(max_sum, now_sum - min_sum)
            min_sum = min(min_sum, now_sum)
            
        return max_sum