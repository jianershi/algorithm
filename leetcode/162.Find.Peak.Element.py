"""
162. Find Peak Element
https://leetcode.com/problems/find-peak-element/

same question

852. Peak Index in a Mountain Array
https://leetcode.com/problems/peak-index-in-a-mountain-array/
"""

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] < nums[mid + 1]:
                start = mid + 1
            else:
                end = mid
        return start
