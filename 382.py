"""
382. Triangle Count
a+b > c
any two side larger than the third one
need to be smaller 2.
so
target from n-1 -> 0
[3, 4, 6, 7]
[       ] ^
if 3 + 6 > 7:
    then 3, 4, all > 7

only need total number but don't need specific ways
"""
class Solution:
    """
    @param S: A list of integers
    @return: An integer
    """
    def triangleCount(self, nums):
        # write your code here
        nums = sorted(nums)
        n = len(nums)
        count = 0
        for i in range(n - 1, -1, -1):
            left, right = 0, i - 1
            while left < right: # < or < =? <
                if left < right and nums[left] + nums[right] > nums[i]:
                    count += right - left
                    right -= 1
                if left < right and nums[left] + nums[right] <= nums[i]:
                    left += 1
        return count
s = Solution()
S = [2,2,2,2]
print(s.triangleCount(S))
