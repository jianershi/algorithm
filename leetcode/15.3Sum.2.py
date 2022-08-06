"""
57. 3Sum
https://www.lintcode.com/problem/3sum/description

15. 3Sum
https://leetcode.com/problems/3sum/

working solution, but it's a bit messy
basically store the result in a set,
then for each 3 number put in, pre-sort them
so there will be no duplicate
convert back to list to return

the other solution is way cleaner
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pairs = set()
        for i in range(len(nums)):
            hash = set()
            for j in range(i + 1, len(nums)):
                if -nums[i] - nums[j] in hash:
                    pairs.add(tuple(sorted([nums[i], -nums[i] - nums[j], nums[j]])))
                hash.add(nums[j])
        return list(pairs)