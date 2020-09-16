"""
604. Window Sum

https://www.lintcode.com/problem/window-sum/description
"""

class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):
        n = len(nums)
        right = 0
        curr_sum = 0
        result = []
        for left in range(n):
            while right < n and right - left < k:
                curr_sum += nums[right]
                right += 1
            result.append(curr_sum)
            if right >= n:
                break
            curr_sum -= nums[left]
        return result
