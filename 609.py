"""
609. Two Sum - Less than or equal to target

"""
class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """
    def twoSum5(self, nums, target):
        # write your code here
        nums.sort()
        left, right = 0, len(nums) - 1
        total_pairs = 0
        while left < right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                total_pairs += right - left
                """
                target = 24
                2, 7, 11, 15, 16
                ^              ^
                2-7 2-11 2-15 2-16
                """
                left += 1

        return total_pairs
