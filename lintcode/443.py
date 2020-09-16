"""
443. Two Sum - Greater than target

https://www.lintcode.com/problem/two-sum-greater-than-target/description
"""

class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: an integer
    """
    def twoSum2(self, nums, target):
        # write your code here
        nums = sorted(nums)
        n = len(nums)
        count = 0

        left, right = 0, n -1
        while left < right:
            if left < right and nums[left] + nums[right] > target:
                count += right - left
                right -= 1
            if left < right and nums[left] + nums[right] <= target:
                left += 1
        return count
