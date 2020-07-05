"""
400. Maximum Gap
https://www.lintcode.com/problem/maximum-gap/description?_from=ladder&&fromId=106

O(n)

https://leetcode.com/problems/maximum-gap/
https://www.lintcode.com/problem/maximum-gap/description?_from=ladder&&fromId=106

为什么bucket size可以取ceiling: 因为[0, 5.5) ->[0, 6）最大区间也是5, 因为是整数的关系。所以可以这么做。
取floor的话得加一条特判 max_val - min_val == 1
"""
import math
class Solution:
    """
    @param nums: an array of integers
    @return: the maximun difference
    """
    def maximumGap(self, nums):
        # write your code here
        if not nums or len(nums) < 2:
            return 0

        n = len(nums)
        max_val, min_val = max(nums), min(nums)
        max_gap = 0

        if max_val == min_val:
            return 0
        if max_val - min_val == 1:
            return 1
            
        bucket_size = int(math.floor((max_val - min_val) / (n - 1)))
        num_of_buckets = n + 1
        
        # bucket_size = int(math.ceil((max_val - min_val) / (n - 1)))
        # num_of_buckets = n

        bucket_min = [sys.maxsize] * num_of_buckets
        bucket_max = [-sys.maxsize] * num_of_buckets
        
        for num in nums:
            i = (num - min_val) // bucket_size
            if num < bucket_min[i]:
                bucket_min[i] = num
            if num > bucket_max[i]:
                bucket_max[i] = num

        for i in range(1, num_of_buckets):
            if bucket_min[i] == sys.maxsize or bucket_max[i] == -sys.maxsize:
                #bucket empty
                bucket_min[i] = bucket_min[i - 1]
                bucket_max[i] = bucket_max[i - 1]

            max_gap = max(max_gap, bucket_min[i] - bucket_max[i - 1])

        return max_gap

