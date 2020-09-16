"""
617. Maximum Average Subarray II
https://www.lintcode.com/problem/maximum-average-subarray-ii/description?_from=ladder&&fromId=106
LTE
"""
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

        prefix_sum = self.cal_prefix_sum(nums)

        start, end = min(nums), max(nums)
        while start + 1e-5 < end: #double cannot use +1 any more
            mid = (start + end) / 2
            if self.exist(mid, nums, k, prefix_sum):
                start = mid
            else:
                end = mid
        if self.exist(end, nums, k, prefix_sum):
            return end
        if self.exist(start, nums, k, prefix_sum):
            return start
        return 0

    def cal_prefix_sum(self, nums):
        n = len(nums)
        prefix_sum = [0] * n
        prefix_sum[0] = nums[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]
        return prefix_sum

    """
    这个方法行不通。因为我想当于每次判断在遍历右侧端点的同时我还在遍历做端点。还是O(n^2)，而这里必须做到O(n)才可以让总体时间变成 O(nlogn),不然和直接遍历开始结束+前缀和O(n^2)的方法就没有区别了。
    """
    def exist(self, mid, nums, k, prefix_sum):
        n = len(nums)
        for r in range(n):
            l = 0
            while r - l + 1 >= k:
                if l == 0:
                    if prefix_sum[r] >= mid * (r - l + 1):
                        return True
                elif prefix_sum[r] - prefix_sum[l - 1] >= mid * (r - l + 1):
                    return True
                l += 1
        return False

s = Solution()
nums = [1,12,-5,-6,50,3]
k = 3

print(s.maxAverage(nums, k))
# print(s.exist(26, nums,k))
