"""
283. Move Zeroes
https://leetcode.com/problems/move-zeroes/
https://leetcode.com/problems/move-zeroes/discuss/172432/THE-EASIEST-but-UNUSUAL-snowball-JAVA-solution-BEATS-100-(O(n))-+-clear-explanation

snowball solution
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        snowball_size = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                snowball_size += 1
            elif snowball_size > 0:
                temp = nums[i]
                nums[i] = 0
                nums[i - snowball_size] = temp
        