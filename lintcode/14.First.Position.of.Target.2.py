"""
14. First Position of Target
https://www.lintcode.com/problem/14/
"""
from typing import (
    List,
)

class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """
    def binary_search(self, nums: List[int], target: int) -> int:
        # write your code here
        if not nums:
            return -1
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] == target:
                end = mid #trying to find first position, so this may or may not be the result
            else:
                end = mid - 1
        
        if nums[start] == target:
            return start
        return -1