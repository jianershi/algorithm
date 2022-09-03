"""
611. Valid Triangle Number
a+b > c
any two side larger than the third one
need to be smaller 2.
so
target from n-1 -> 0
[3, 4, 6, 7]
[       ] ^
if 3 + 6 > 7:
    then moving left index 3, 4, all + set right index [6] > 7
    count all pairs at once using right - left
    once done, moving right index leftwards 1 digit
    
only need total number but don't need specific ways
"""
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        count = 0
        for i in range(len(nums) - 1, -1, -1):
            left, right = 0, i - 1
            while left < right:
                if left < right and nums[left] + nums[right] > nums[i]:
                    count += right - left
                    right -= 1
                if left < right and nums[left] + nums[right] <= nums[i]:
                    left += 1
        
        return count
        