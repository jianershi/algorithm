"""
533. Two Sum - Closest to target
[-1, 2, 1, -4] and target = 4
-4, -1, 3, 9, 10
^       ^
6   4   2 > 0
5   4   1 > 0
-1  4   3 < 0

whenever the sign flipped, the search can stop
or if the diff becomes bigger, the search can stop

"""
import sys
class Solution:
    """
    @param nums: an integer array
    @param target: An integer
    @return: the difference between the sum and the target
    """
    def twoSumClosest(self, nums, target):
        # write your code here
        nums = sorted(nums)
        # print (nums)
        min_diff = sys.maxsize
        left, right = 0, len(nums) - 1

        while left < right:
            while left < right and nums[left] + nums[right] < target:
                diff = abs(nums[left] + nums[right] - target)
                min_diff = min(min_diff, diff)
                left += 1
            while left < right and nums[left] + nums[right] > target:
                diff = abs(nums[left] + nums[right] - target)
                min_diff = min(min_diff, diff)
                right -= 1
            if left < right:
                diff = abs(nums[left] + nums[right] - target)
                min_diff = min(min_diff, diff)
                if nums[left] == nums[right]:
                    break
                left += 1
                right -= 1
        return min_diff

s = Solution()
nums = [1,0,-1]

target = 0
print(s.twoSumClosest(nums,target))
