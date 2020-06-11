"""
1879. Two Sum VII
https://www.lintcode.com/problem/two-sum-vii/description
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

        n = len(nums)
        smallest_index, biggest_index = None, None
        smallest, biggest = sys.maxsize, -sys.maxsize
        for i, num in enumerate(nums):
            if num < smallest:
                smallest = num
                smallest_index = i
            if num > biggest:
                biggest = num
                biggest_index = i

        left, right = smallest_index, biggest_index
        while 0 <= left < n and 0 <= right < n and nums[left] < nums[right]:
            if nums[left] + nums[right] < target:
                left = self.find_next_bigger(left, nums)
                if left == -1:
                    break
                continue
            if nums[left] + nums[right] > target:
                right = self.find_next_smaller(right, nums)
                if right == -1:
                    break
                continue
            if nums[left] + nums[right] == target:
                results.append(sorted([left, right]))
                left = self.find_next_bigger(left, nums)
                if left == -1:
                    break
                right = self.find_next_smaller(right, nums)
                if right == -1:
                    break

        return results

    """
    return sucess, then number
    """
    def find_next_bigger(self, i, nums):
        n = len(nums)
        if not 0 <= i < n:
            return -1
        if nums[i] >= 0:
            for j in range(i + 1, n):
                if nums[j] >= 0:
                    return j
            return -1
        elif nums[i] < 0:
            for j in range(i - 1, -1, -1):
                if nums[j] < 0:
                    return j
            for j in range(n):
                if nums[j] >= 0:
                    return j
            return -1

    def find_next_smaller(self, i, nums):
        n = len(nums)
        if not 0 <= i < n:
            return -1
        if nums[i] >= 0:
            for j in range(i - 1, -1 , -1):
                if nums[j] >= 0:
                    return j
            for j in range(n):
                if nums[j] < 0:
                    return j
            return -1
        elif nums[i] < 0:
            for j in range(i + 1, n):
                if nums[j] < 0:
                    return j
            return -1
