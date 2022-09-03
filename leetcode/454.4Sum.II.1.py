"""
454. 4Sum II
https://leetcode.com/problems/4sum-ii/

https://www.jiuzhang.com/solution/4sum-ii
"""
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n = len(nums1)
        
        total = 0
        counter = {}
        for a in nums1:
            for b in nums2:
                counter[a + b] = counter.get(a + b, 0) + 1
        
        for c in nums3:
            for d in nums4:
                    total += counter.get(- c - d, 0)
        
        return total