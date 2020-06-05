"""
5. Kth Largest Element
Quick Select

"""
class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        # write your code here
        if not nums:
            return -1
        return self.quick_select(nums, 0, len(nums) - 1, n)

    def quick_select(self, nums, start, end, k):
        if start == end:
            return nums[start]

        left, right = start, end
        pivot = nums[(left + start) // 2]

        while left <= right:
            while left <= right and nums[left] > pivot:
                left += 1
            while left <= right and nums[right] < pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        if start + k - 1 <= right:
            return self.quick_select(nums, start, right, k)
        if start + k - 1 >= left:
            return self.quick_select(nums, left, end, k - (left - start))
        return nums[right + 1]
