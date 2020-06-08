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
        right = 0
        n = len(nums)
        sum = 0
        min_length = n + 1
        for left in range(n):
            while right < n and sum < s:
                sum += nums[right]
                right += 1
            if sum >= s:
                min_length = min(min_length, right - left) #right is pointing to next position already.

            sum -= nums[left]

        return min_length if min_length != n + 1 else -1
