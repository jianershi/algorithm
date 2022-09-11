"""
31. Partition Array
https://www.lintcode.com/problem/31/

notice that the requirement is to return the first element such that A[i] >= k,
so if we are using two pointers, the left pointer must stop when it first see an element that is A[i] == k,
keep moving the right pointer leftwards until it passed the left pointer. 
wheverever the leftpointer points is the first element that is A[i] >= k
"""
class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        left, right = 0, len(nums) - 1
        while left <= right:
            while left <= right and nums[left] < k:
                left += 1
            while left <= right and nums[right] >= k:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return left

s = Solution()
nums = []
k = 9
print(s.partitionArray(nums,k))
