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
            diff = abs(nums[left] + nums[right] - target)
            min_diff = min(min_diff, diff)
            if left < right and nums[left] + nums[right] < target:
                left += 1
            elif left < right and nums[left] + nums[right] > target:
                right -= 1
            else:
                break
        return min_diff

s = Solution()
nums = [1,0,-1]

target = 0
print(s.twoSumClosest(nums,target))
