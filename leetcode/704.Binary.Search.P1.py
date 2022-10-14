"""
704. Binary Search
https://leetcode.com/problems/binary-search/

457 · Classical Binary Search
https://www.lintcode.com/problem/457/

pattern 1:
lower bound mid
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        start, end = 0, len(nums) - 1
        while start < end:
            mid = start + (end - start) // 2 #using lower bound
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] == target:
                end = mid
            else:
                end = mid - 1
        
        if nums[start] == target:
            return start
        return -1