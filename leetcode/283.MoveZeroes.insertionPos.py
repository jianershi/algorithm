"""
283. Move Zeroes
https://leetcode.com/problems/move-zeroes/

https://leetcode.com/problems/move-zeroes/discuss/72011/Simple-O(N)-Java-Solution-Using-Insert-Index

insertion positions
only considering non zero members
then attach remaining as zero
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        insertion_pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insertion_pos] = nums[i]
                insertion_pos += 1
        
        for i in range(insertion_pos, len(nums)):
            nums[i] = 0