"""
969. Pancake Sorting
https://leetcode.com/problems/pancake-sorting/

* notice this is standard pancake sorting, not the solution to the problem

O(n^2) time complexity
O(1) space
"""
class Solution:
    def pancakeSort(self, arr: list[int]) -> list[int]:
        for curr_len in range(len(arr), 1, -1):
            self.pancake_sort(arr, curr_len - 1)
        
    def pancake_sort(self, nums, last_index):
        flip_index = nums.index(max(nums[:last_index + 1]))
        self.flip(nums, flip_index)
        self.flip(nums, last_index)
        
    def flip(self, nums, flip_index):
        nums[:flip_index + 1] = nums[:flip_index + 1][::-1] 


import unittest
class Test(unittest.TestCase):
    s = Solution()

    def test1(self):
        nums =  [23, 10, 20, 11, 12, 6, 7]
        target = [6, 7, 10, 11, 12, 20, 23]
        self.s.pancakeSort(nums)
        self.assertEqual(target, nums)

    def test2(self):
        nums =  [0, 1, 1, 0, 0 ]
        target = [0, 0, 0, 1, 1]
        self.s.pancakeSort(nums)
        self.assertEqual(target, nums)

if __name__ == '__main__':
    unittest.main()

