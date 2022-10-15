"""
159 · Find Minimum in Rotated Sorted Array
https://www.lintcode.com/problem/159

153. Find Minimum in Rotated Sorted Array
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
"""
"""
algorithm bisection method -> o(logn)
elements are unique
there must be a unique minimu element
it is also sorted, that means finding the pivot = finding the minimum element of the array
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
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
        