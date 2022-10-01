"""
144.Interleaving.Positive.and.Negative.Numbers
https://www.lintcode.com/problem/144/

o(n) time
first move either positive or negative numbers to a side using partition
then interleave them

partition using pointers moving in the same direction

"""
from typing import (
    List,
)

class Solution:
    """
    @param a: An integer array.
    @return: nothing
    """
    def rerange(self, a: List[int]):
        # write your code here
        pos_count, neg_count = 0, 0
        for num in a:
            if num >= 0:
                pos_count += 1
            else:
                neg_count += 1
        
        self.partition(a, pos_count >= neg_count)
        print(a)
        self.interleave(a, pos_count == neg_count)
    
    def partition(self, nums, start_positive):
        flag = 1 if start_positive else -1
        pos_idx = 0
        for i in range(len(nums)):
            if nums[i] * flag >= 0:
                nums[pos_idx], nums[i] = nums[i], nums[pos_idx]
                pos_idx += 1

    def interleave(self, nums, same_length):
        # xxxooo
        #   o  x
        if same_length:
            l, r = 1, len(nums) - 2
        # xxxxooo
        else:
            l, r = 1, len(nums) - 1
        
        while l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 2
            r -= 2