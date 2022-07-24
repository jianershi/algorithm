"""
53. Maximum Subarray

d[i] : max subarray sum **including** ith digit
d[i] = d[i-1] + x[i] if d[i - 1] > 0 else x[i]
solution max(d[p])

o(n)
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        d = [0] * len(nums)
        d[0] = nums[0]
        for i in range(1, len(nums)):
            if (d[i - 1] > 0):
                d[i] = d[i - 1] + nums[i]
            else:
                d[i] = nums[i]
        return max(d)