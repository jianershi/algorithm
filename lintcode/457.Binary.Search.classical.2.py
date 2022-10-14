"""
704. Binary Search
https://leetcode.com/problems/binary-search/

457 · Classical Binary Search
https://www.lintcode.com/problem/457/
"""

class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def findPosition(self, nums, target):
        # write your code here
        if not nums:
            return -1
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] == target:
                end = mid
            else:
                end = mid - 1
        
        if nums[start] == target:
            return start
        return -1