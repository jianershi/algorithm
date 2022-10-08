"""
704. Binary Search
https://leetcode.com/problems/binary-search/

457 · Classical Binary Search
https://www.lintcode.com/problem/457/
"""
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if not nums:
            return -1
        
        start, end = 0, len(nums) - 1
        
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            elif nums[mid] == target:
                end = mid
            else:
                end = mid
    
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1
    
import unittest
class Test(unittest.TestCase):
    s = Solution()

    def test1(self):
        nums = [0,1]
        target = 1
        self.assertEqual(1, self.s.search(nums, target))

if __name__ == '__main__':
    unittest.main()