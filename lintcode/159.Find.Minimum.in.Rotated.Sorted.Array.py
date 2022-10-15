"""
159 · Find Minimum in Rotated Sorted Array
https://www.lintcode.com/problem/159

153. Find Minimum in Rotated Sorted Array
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
"""
from typing import (
    List,
)

class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def find_min(self, nums: List[int]) -> int:
        # write your code here
        start, end = 0, len(nums) - 1 
        while start < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid + 1
            elif nums[mid] == nums[end]:
                end = mid #not sure if this matters
            else:
                end = mid

        return nums[start]