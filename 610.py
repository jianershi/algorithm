"""
610. Two Sum - Difference equals to target
https://www.lintcode.com/problem/two-sum-difference-equals-to-target/description
binary search
"""
class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [num1, num2] (num1 < num2)
    """
    def twoSum7(self, nums, target):
        # write your code here
        if not nums or len(nums) < 2:
            return (-1, -1)

        n = len(nums)
        target = abs(target)
        #nums[right] - nums[left] = target

        for i in range(n):
            result = self.binary_search(nums, i + 1, n - 1, target + nums[i])
            if result != -1:
                return nums[i], result

        return (-1, -1)

    def binary_search(self, nums, start, end, target):
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            else:
                end = mid
        if nums[start] == target:
            return nums[start]
        if nums[end] == target:
            return nums[end]
        return -1
