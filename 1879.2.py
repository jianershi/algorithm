"""
1879. Two Sum VII
https://www.lintcode.com/problem/two-sum-vii/description
binary search

"""
import sys
class Solution:
    """
    @param nums: the input array
    @param target: the target number
    @return: return the target pair
    """
    def twoSumVII(self, nums, target):
        # write your code here
        results = []

        if not nums:
            return results

        results = []
        n = len(nums)

        for i in range(n):
            result = self.binary_search(nums, i + 1, n - 1, target - nums[i])
            if result != None:
                results.append(sorted([i, result]))
        return results

    def binary_search(self, nums, start, end, target):
        if start > end:
            return None
        left, right = start, end
        while left + 1 < right:
            mid = (left + right) // 2
            if abs(nums[mid]) < abs(target):
                left = mid
            elif abs(nums[mid]) > abs(target):
                right = mid
            else:
                right = mid
        if nums[left] == target:
            return left
        if left > start and nums[left - 1] == target:
            return left - 1
        if nums[right] == target:
            return right
        if right < end and nums[right + 1] == target:
            return right + 1
        return None
