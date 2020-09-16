"""
617. Maximum Average Subarray II
https://www.lintcode.com/problem/maximum-average-subarray-ii/description?_from=ladder&&fromId=106
"""
import sys
class Solution:
    """
    @param nums: an array with positive and negative numbers
    @param k: an integer
    @return: the maximum average
    """
    def maxAverage(self, nums, k):
        # write your code here
        if not nums or k > len(nums):
            return 0

        start, end = min(nums), max(nums)
        while start + 1e-5 < end: #double cannot use +1 any more
            mid = (start + end) / 2
            if self.exist(mid, nums, k):
                start = mid
            else:
                end = mid
        if self.exist(end, nums, k):
            return end
        if self.exist(start, nums, k):
            return start
        return 0

    def exist(self, avg, nums, k):
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        min_prefix_sum_left = sys.maxsize

        for i in range(1, k):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1] - avg
        for r in range(k, n + 1):
            prefix_sum[r] = prefix_sum[r - 1] + nums[r - 1] - avg
            min_prefix_sum_left = min(min_prefix_sum_left, prefix_sum[r - k])

            if prefix_sum[r] - min_prefix_sum_left >= 0:
                return True
        return False


s = Solution()
nums = [1,12,-5,-6,50,3]
k = 3

print(s.maxAverage(nums, k))
# print(s.exist(26, nums,k))
