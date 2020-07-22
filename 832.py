"""
832. Count Negative Number
https://www.lintcode.com/problem/count-negative-number/description?_from=ladder&&fromId=152
o(nlogm)
"""
class Solution:
    """
    @param nums: the sorted matrix
    @return: the number of Negative Number
    """
    def countNumber(self, nums):
        # Write your code here
        count = 0
        if not nums:
            return count
        n = len(nums)

        for row in nums:
            if len(row) > 0 and row[0] >= 0:
                continue
            count += self.binary_search(row, len(row))

        return count
        
    def binary_search(self, nums, m):
        start, end = 0, m - 1
        left, right = start, end
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < 0:
                left = mid
            elif nums[mid] > 0:
                right = mid
            else:
                right = mid
        if nums[right] < 0:
            return right + 1
        if nums[left] < 0:
            return left + 1
        return 0