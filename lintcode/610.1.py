"""
610. Two Sum - Difference equals to target
https://www.lintcode.com/problem/two-sum-difference-equals-to-target/description
two pointer. same direction
"""
class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [num1, num2] (num1 < num2)
    """
    def twoSum7(self, nums, target):
        if not nums or len(nums) < 2:
            return -1, -1
        n = len(nums)
        target = abs(target)

        j = 0
        for i in range(n):
            j = max(j, i + 1)
            while j < n and nums[j] - nums[i] < target:
                j += 1
            if j >= n:
                break
            if nums[j] - nums[i] == target:
                return nums[i], nums[j]

        return -1, -1
