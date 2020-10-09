"""
57. 3Sum
https://www.lintcode.com/problem/3sum/description

15. 3Sum
https://leetcode.com/problems/3sum/

sort to solve duplicate
-a = b + c
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.two_sum(-nums[i], i + 1, nums, res)
        return res
    
    def two_sum(self, target, start_index, nums, res):
        last = None
        seen = set()
        for i in range(start_index, len(nums)):
            if target - nums[i] in seen and last != nums[i]:
                res.append((-target, target - nums[i], nums[i]))
                last = nums[i]
            seen.add(nums[i])