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
        for i in range(31):
            one_count = 0
            for i in range(n):
                one_count += nums[i] & 1
                nums[i] >>= 1
            res += one_count * (n - one_count)
        return res