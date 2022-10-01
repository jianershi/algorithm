"""
75. Sort Colors
https://leetcode.com/problems/sort-colors/

thought1:
3 points ? is it possible?
problem is i don't know when to stop <- i don't know the position of the center pointer

can i just use quicksort?

hint: two pass

then: i only sort one side first, then move eveyrthing else to the other side
then do another pass sorting the other other side
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = self.partition(nums, 0, len(nums) - 1, 0)
        self.partition(nums, l, len(nums) - 1, 1)
        
    """
    parition in place
    return the first index that is not partioned
    """
    def partition(self, nums, start, end, anchor):
        l, r = start, end
        while l <= r:
            while l <= r and nums[l] == anchor:
                l += 1
            while l <= r and nums[r] != anchor:
                r -= 1
            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        return l
        
        