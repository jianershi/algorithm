"""
587. Two Sum - Unique pairs
"""
class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        nums = sorted(nums)

        left, right = 0, len(nums) - 1
        last_pair = (None, None)
        count = 0
        while left < right:
            while left < right and (nums[left], nums[right]) == last_pair:
                left += 1
                right -= 1
            while left < right and nums[left] + nums[right] < target:
                left += 1
            while left < right and nums[left] + nums[right] > target:
                right -= 1
            if left < right and nums[left] + nums[right] == target:
                count += 1
                last_pair = (nums[left], nums[right])
        return count
