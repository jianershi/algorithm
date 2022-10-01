"""
75. Sort Colors
https://leetcode.com/problems/sort-colors/

ok follow up:
1pass algorithm with constant extra space

idea:
only sort left:0 and right part:2, anytime 1 appears, take it out, and put it into a new array

in the end, 0 and 2 are sorted
and 1 can reattach back to the middle

**this solution is wrong**
because it will stuck in the middle in the following situation

0 1 2 ... 1 1 2
^             ^
l             r 
  ^         ^
  l         r
  both pointers stopped here waiting to be replaced
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        extra = []
        
        l, r = 0, len(nums) - 1
        while l <= r:
            while l <= r and nums[l] == 0:
                l += 1
            while l <= r and nums[r] == 2:
                r -= 1
            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                if nums[l] == 0 and nums[r] == 2:
                    l += 1
                    r -= 1
                else: #means at least one of those index has color 1
                    if nums[l] == 1 and nums[r] == 1:
                        if l != r:
                            extra.append(1)
                            extra.append(1)
                        continue
                    if nums[l] == 1:
                        if l != r:
                            extra.append(1)
                        r -= 1
                    elif nums[r] == 1:
                        if l != r:
                            extra.append(1)
                        l += 1

        print(l, r, nums, extra)
        for i in range(len(extra)):
            nums[l + i] = 1
                        
                    
        