"""
400. Maximum Gap
https://www.lintcode.com/problem/maximum-gap/description?_from=ladder&&fromId=106

O(nlogn)
"""
class Solution:
    """
    @param nums: an array of integers
    @return: the maximun difference
    """
    def maximumGap(self, nums):
        # write your code here
        if not nums:
            return 0

        nums = sorted(nums)
        n = len(nums)

        max_gap = 0
        for i in range(1, n):
            max_gap = max(max_gap, nums[i] - nums[i - 1])
        return max_gap

