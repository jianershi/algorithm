"""
461. Kth Smallest Numbers in Unsorted Array

https://www.lintcode.com/problem/kth-smallest-numbers-in-unsorted-array/description
"""
class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """
    def kthSmallest(self, k, nums):
        return self.quick_select(nums, 0, len(nums) - 1, k)

    def quick_select(self, nums, start, end, k):
        # if start == end:
            # return nums[start]

        left, right = start, end
        pivot = nums[(start + end) // 2]

        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        if right - start >= k - 1:
            return self.quick_select(nums, start, right, k)
        if left - start < k:
            return self.quick_select(nums, left, end, k - (left - start))
        return nums[right + 1]
