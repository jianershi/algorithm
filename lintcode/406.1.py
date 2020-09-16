"""
406. Minimum Size Subarray Sum
"""
import sys
class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """
    def minimumSize(self, nums, s):
        left = 0
        n = len(nums)
        sum = 0
        min_length = n + 1
        for right in range(n):
            sum += nums[right]
            while sum >= s:
                min_length = min(min_length, right - left + 1)
                sum -= nums[left]
                left += 1

        return min_length if min_length != n + 1 else -1
