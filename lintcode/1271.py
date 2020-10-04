"""
1217. Total Hamming Distance
https://www.lintcode.com/problem/total-hamming-distance/description
tle:
o(n^2 * 30) <- 1e9 ~~ 2<<30. so every search takes 30 in worst case. roughly o(10^9) tle
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
        for i in range(n):
            for j in range(i, n):
                c = nums[i] ^ nums[j]
                while c > 0:
                    res +=  c & 1
                    c >>= 1
        return res