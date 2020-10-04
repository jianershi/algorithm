"""
1217. Total Hamming Distance
https://www.lintcode.com/problem/total-hamming-distance/description
o(n * 30)
"""
class Solution:
    """
    @param nums: the gievn integers
    @return: the total Hamming distance between all pairs of the given numbers
    """
    def totalHammingDistance(self, nums):
        # Write your code here
        res = 0
        n = len(nums)
        ones = [0] * 30
        for num in nums:
            j = 29
            while num > 0:
                ones[j] += num & 1
                num >>= 1
                j -= 1
        for i in range(30):
            res += ones[i] * (len(nums) - ones[i])
        return res