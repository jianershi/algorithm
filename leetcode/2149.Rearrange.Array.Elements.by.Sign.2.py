"""
2149. Rearrange Array Elements by Sign
https://leetcode.com/problems/rearrange-array-elements-by-sign/
easier solution, since pos and neg are of the same length
https://leetcode.com/problems/rearrange-array-elements-by-sign/discuss/1724474/Python3-or-easy-to-understand-or-More-Optimized
"""
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        p = 0
        n = 1
        for num in nums:
            if num >= 0:
                result[p] = num
                p += 2
            else:
                result[n] = num
                n += 2
        return result