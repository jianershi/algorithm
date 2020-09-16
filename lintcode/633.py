"""
633. Find the Duplicate Number
https://www.lintcode.com/problem/find-the-duplicate-number/description?_from=ladder&&fromId=106
九章强化班
"""
class Solution:
    """
    @param nums: an array containing n + 1 integers which is between 1 and n
    @return: the duplicate one
    """
    def findDuplicate(self, nums):
        # write your code here
        #注意。这道题二分的是范围。因为只有范围是有序的。本身数组是无序的。
        start, end = 1, len(nums)
        while start + 1 < end:
            mid = (start + end) // 2
            if self.count_eq_smaller(mid, nums) > mid:
                end = mid
            else:
                start = mid
        if self.count_eq_smaller(start, nums) > start:
            return start
        return end

    def count_eq_smaller(self, target, nums):
        count = 0
        for num in nums:
            if num <= target:
                count +=1
        return count
