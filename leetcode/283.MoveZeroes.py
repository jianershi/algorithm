"""
283. Move Zeroes
https://leetcode.com/problems/move-zeroes/

"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
        for i in range(len(nums)):
            while (nums[i] == 0 and zero_count > 0): #this deals with two consecutive zeros
                self.move_back(i, nums)
                zero_count -= 1
        
    def move_back(self, idx, nums):
        nums[idx:len(nums) - 1] = nums[idx + 1:len(nums)]
        nums[len(nums) - 1] = 0