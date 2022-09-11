"""
2149. Rearrange Array Elements by Sign
https://leetcode.com/problems/rearrange-array-elements-by-sign/

inline version
lintcode 144
144 · Interleaving Positive and Negative Numbers
https://www.lintcode.com/problem/144/
"""
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos_array = []
        neg_array = []
        for num in nums:
            if num >= 0:
                pos_array.append(num)
            else:
                neg_array.append(num)
        
        if len(pos_array) >= len(neg_array):
            return self.assembleArray(pos_array, neg_array)
        else:
            return self.aseembleArray(neg_array, pos_array)
              
    def assembleArray(self, longArray, shortArray):
        result = []
        l, r = 0, 0
        while r < len(shortArray):
            result.append(longArray[l])
            result.append(shortArray[r])
            l += 1
            r += 1
        while l < len(longArray):
            result.append(longArray[l])
            l += 1
        return result