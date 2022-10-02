"""
969. Pancake Sorting
https://leetcode.com/problems/pancake-sorting/

* notice this is standard pancake sorting, not the solution to the problem

O(n^2) time complexity
O(1) space
"""
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []
        for curr_len in range(len(arr), 1, -1):
            self.pancake_sort(arr, curr_len - 1, result)
        print(arr)
        return result
        
    def pancake_sort(self, nums, last_index, res):
        flip_index = nums.index(max(nums[:last_index + 1]))
        self.flip(nums, flip_index)
        self.flip(nums, last_index)
        res.append(flip_index + 1)
        res.append(last_index + 1)
        
    def flip(self, nums, flip_index):
        nums[:flip_index + 1] = nums[:flip_index + 1][::-1] 