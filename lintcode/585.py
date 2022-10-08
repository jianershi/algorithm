"""
585. Maximum Number in Mountain Sequence

852. Peak Index in a Mountain Array
https://leetcode.com/problems/peak-index-in-a-mountain-array/
"""
class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountainSequence(self, nums):
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] > nums[mid + 1]:
                end = mid
            else:
                start = mid

        return max(nums[start], nums[end])
