"""
14. First Position of Target

"""
class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """
    def binarySearch(self, nums, target):
        # write your code here
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            elif nums[mid] == target:
                end = mid #because want to find the first target, there might be a number before mid, seek on the left side
            else:
                end = mid

        #first position of target. so search start first
        if nums[start] == target:
            return start

        if nums[end] == target:
            return end

        return -1
