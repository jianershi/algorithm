"""
406. Minimum Size Subarray Sum
"""
import sys
class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """
    def minimumSize(self, nums, s):
        # write your code here
        prefix_sum = [0]
        sum = 0
        for i in range(1, len(nums) + 1):
            sum += nums[i - 1]
            prefix_sum.append(sum)

        """
            01234
            i   j
        xxxxxxxxo
        """
        minimum_length = sys.maxsize
        right = 0

        for left in range(len(nums)):
            while right < len(nums) and prefix_sum[right + 1] - prefix_sum[left] < s:
                right += 1
            if right >= len(nums):
                break
            minimum_length = min(minimum_length, right - left + 1)
        return minimum_length if minimum_length != sys.maxsize else -1
