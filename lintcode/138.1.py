"""
138. Subarray Sum
https://www.lintcode.com/problem/subarray-sum/description
九章强化班C7

xxxxxxxxixxxxxxj

sum(i:j+1) == 0:
prefix_sum(j) - prefix_sum(i - 1) = 0
prefix_sum(j) = prefix_sum(i - 1)
"""
class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        prefix_sum = {0:-1}
        now_sum = 0
        for i, num in enumerate(nums):
            now_sum += num
            if now_sum in prefix_sum:
                return (prefix_sum[now_sum] + 1, i)
            prefix_sum[now_sum] = i