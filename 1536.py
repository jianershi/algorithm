"""
1536. Find First and Last Position of Element in Sorted Array
https://www.lintcode.com/problem/find-first-and-last-position-of-element-in-sorted-array/description
"""
class Solution:
    """
    @param nums: the array of integers
    @param target:
    @return: the starting and ending position
    """
    def searchRange(self, nums, target):
        # Write your code here.
        if not nums:
            return -1, -1

        return self.find_first(nums, target), self.find_last(nums, target)

    def find_first(self, nums, target):
        n = len(nums)
        start, end = 0, n - 1

        start_pos, end_pos = None, None
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            elif nums[mid] > target:
                end = mid
            else: # == find first position
                end = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1

    def find_last(self, nums, target):
        n = len(nums)
        start, end = 0, n - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            elif nums[mid] > target:
                end = mid
            else: # == find last position
                start = mid
        if nums[end] == target:
            return end
        if nums[start] == target:
            return start
        return -1
