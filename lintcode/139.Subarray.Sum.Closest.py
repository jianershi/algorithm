"""
139. Subarray Sum Closest
https://www.lintcode.com/problem/subarray-sum-closest/description
九章强化班C7 Subarray Sum Follow Up

....i.....j
sum from i to j i, j included
prefix_sum(j + 1) - prefix_sum(i)

0,1,2
  ^
  prefix_sum(2), prefix_sum(previous kth digit)
"""
import sys
class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySumClosest(self, nums):
        # write your code here
        if not nums:
            return [-1, -1]

        prefix_sum = self.cal_prefix_sum(nums) #(prefix_sum, #index)
        prefix_sum.sort()

        min_distance = sys.maxsize
        min_index = [None, None]
        for i in range(len(prefix_sum) - 1, 0, -1):
            now_dist = prefix_sum[i][0] - prefix_sum[i - 1][0]
            if now_dist < min_distance:
                min_distance = now_dist
                left = min([prefix_sum[i][1], prefix_sum[i - 1][1]])
                right = max([prefix_sum[i][1], prefix_sum[i - 1][1]]) - 1
                min_index = [left, right]
                
        return min_index

    """
    prefix_sum (previous ith sum, ith)
    """
    def cal_prefix_sum(self, nums):
        n = len(nums)
        prefix_sum = [None] * (n + 1) 
        prefix_sum[0] = (0, 0)
        for i in range(1, n + 1):
            prefix_sum[i] = (prefix_sum[i - 1][0] + nums[i - 1], i)

        return prefix_sum


