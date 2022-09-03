"""
18. 4Sum
https://leetcode.com/problems/4sum/

https://www.lintcode.com/problem/58/description
"""
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        prev_num = None
        for i in range(len(nums)):
            if prev_num != None and nums[i] == prev_num:
                continue
            prev_num = nums[i]
            threesum_result = self.threeSum(nums, i + 1, target - nums[i])
            if threesum_result == None:
                continue
            result.extend([[nums[i], *x] for x in threesum_result])
        return result
    
    def threeSum(self, nums, starting_index, target):
        result = []
        prev_num = None
        for i in range(starting_index, len(nums)):
            if prev_num != None and nums[i] == prev_num:
                continue
            prev_num = nums[i]
            twosum_result = self.twoSum(nums, i + 1, target - nums[i])
            if twosum_result == None:
                continue
            result.extend([[nums[i], *x] for x in twosum_result])
        return result
    
    def twoSum(self, nums, starting_index, target):
        result = []
        seen = set()
        prev_pair = (None, None)
        for i in range(starting_index, len(nums)):
            if (target - nums[i], nums[i]) == prev_pair:
                continue
            if target - nums[i] in seen:
                result.append([target - nums[i], nums[i]])
                prev_pair = (target - nums[i], nums[i])
            else:
                seen.add(nums[i])
        return result