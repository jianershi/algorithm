"""
454. 4Sum II
https://leetcode.com/problems/4sum-ii/
time limit exceeded
"""

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n = len(nums1)
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        nums3 = sorted(nums3)
        nums4 = sorted(nums4)
        
        count = 0
        
        for i in range(n):
            for j in range(n):
                for l in range(n):
                    for r in range(n):
                        if nums1[i] + nums2[j] + nums3[l] + nums4[r] == 0:
                            count += 1
                            continue
                        if nums1[i] + nums2[j] + nums3[l] + nums4[r] > 0:
                            break
                        
        
        return count