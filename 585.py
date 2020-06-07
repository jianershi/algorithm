"""
585. Maximum Number in Mountain Sequence

"""
class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountainSequence(self, nums):
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid - 1] < nums[mid]:
                start = mid
            elif nums[mid] > nums[mid + 1]:
                end = mid

        return mid
