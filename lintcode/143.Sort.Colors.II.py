"""
143 · Sort Colors II
https://www.lintcode.com/problem/143/

quick sort

o(nlogn)
"""
from typing import (
    List,
)

class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sort_colors2(self, colors: List[int], k: int):
        # write your code here
        self.quick_sort(colors, 0, len(colors) - 1)

    def quick_sort(self, nums, start, end):
        if start >= end:
            return
        l, r = start, end
        pivot = (nums[l] + nums[r]) // 2
        while l <= r:
            while l <= r and nums[l] < pivot:
                l += 1
            while l <= r and nums[r] > pivot:
                r -= 1
            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        self.quick_sort(nums, start, r)
        self.quick_sort(nums, l, end)