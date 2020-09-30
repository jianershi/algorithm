"""
838. Subarray Sum Equals K
https://www.lintcode.com/problem/subarray-sum-equals-k/description
"""
class Solution:
    """
    @param nums: a list of integer
    @param k: an integer
    @return: return an integer, denote the number of continuous subarrays whose sum equals to k
    """
    def subarraySumEqualsK(self, nums, k):
        # write your code here
        seen = {0:1}
        nowSum = 0
        res = 0
        for num in nums:
            nowSum += num
            if nowSum - k in seen:
                res += seen[nowSum - k]
            seen[nowSum] = seen.get(nowSum, 0) + 1
        return res
