"""
34. Find First and Last Position of Element in Sorted Array

https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

dirty solution
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        first = self.findFirst(nums, target)
        last = self.findLast(nums, target)
        if first == -1 or last == -1:
            return [-1, -1]
        
        return [first, last]

    def findFirst(self, nums, target):
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
    
    def findLast(self, nums, target):
        start, end = 0, len(nums) - 1
        
        while start < end:
            mid = (start + end + 1) // 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] == target:
                start = mid
            else:
                end = mid - 1
        
        if nums[end] == target:
            return end
        return -1
    
    
        