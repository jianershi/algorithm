"""
521. Remove Duplicate Numbers in Array
https://www.lintcode.com/problem/remove-duplicate-numbers-in-array/description
"""
class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        if not nums:
            return 0

        n = len(nums)
        nums.sort()
        j = 0
        for i in range(n):
            while j < n and nums[j] == nums[i]:
                j += 1
            if j >= n:
                break
            nums[i + 1] = nums[j]
        return i + 1
