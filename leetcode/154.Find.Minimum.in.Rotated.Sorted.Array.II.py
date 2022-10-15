"""
154. Find Minimum in Rotated Sorted Array II
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

difference
this one has duplicates

worst case scenario, 
[1111111111...101...1111111] <- you have to look through every 1,
this exceed o(logn) to as much as o(n) in worst case
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1 
        while start < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid + 1
            elif nums[mid] == nums[start]:
                end -= 1
                """
                we don't know where the mid falls,
                [111111101]
                 s   m   e
                [111011111]
                 s   m   e
                 since we don't know how to do in this case, we can just shrink end by 1,
                 because, we are tring to find pivot, if mid is pivot, then it doesn't matter we disgarded end since it is the same number
                 we can also **not** do start + 1 
                 because we are comaring mid with end, start could be a different number
                 if we were comparing start with mid, because (start + end) // 2 falls to the left,
                 we might be out of bounds, or they could be actually pointing to the same number, which naturally equals
                 but this will result in another issue
                 [1,2,3,4,5]
                 [2,3,4,5,1]
                  <- we cannot compare mid with start to result to know for sure that pivot is on the right, we have to compare to the end.
                """
            else:
                end = mid
        
        return nums[start]