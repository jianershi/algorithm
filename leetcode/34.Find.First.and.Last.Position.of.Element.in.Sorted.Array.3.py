"""
34. Find First and Last Position of Element in Sorted Array

https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

dirty solution

edge case different method
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        first = self.findFirst(nums, target)
        last = self.findLast(nums, target)
        return [first, last]

    def findFirst(self, nums, target):
        start, end = 0, len(nums) - 1
        first = -1
        
        while start < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] == target:
                end = mid - 1
                first = mid
            else:
                end = mid - 1
        
        if nums[start] == target:
            return start
        return first
    
    def findLast(self, nums, target):
        start, end = 0, len(nums) - 1
        last = -1
        
        while start < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] == target:
                start = mid + 1
                last = mid
            else:
                end = mid - 1
        
        if nums[end] == target:
            return end
        return last