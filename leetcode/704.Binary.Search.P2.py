"""
704. Binary Search
https://leetcode.com/problems/binary-search/

457 · Classical Binary Search
https://www.lintcode.com/problem/457/

pattern 2:
upper bound mid

has to compare end in this case. because could have 
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        start, end = 0, len(nums) - 1
        while start < end:
            mid = start + (end - start + 1) // 2
            if nums[mid] < target:
                start = mid #we cannot use start = mid + 1 because upper bound mid, could result in past largest index
            elif nums[mid] == target:
                start = mid
            else:
                end = mid - 1
        
        if nums[start] == target:
            return start
        return -1