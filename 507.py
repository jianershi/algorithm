"""
507. Wiggle Sort II
https://www.lintcode.com/problem/wiggle-sort-ii/description
九章算法强化班C7..强化班其实没讲。。
1. quick select 找中位数 O(n) -> find kth
2. 3 way partition 分成 > mean = mean < mean 3部分，148. Sort Colors O(n)
3. 答案奇数位 = 这个数组后半部分， 欧数位为前半部分。 https://leetcode.com/problems/wiggle-sort-ii/discuss/77677/O(n)%2BO(1)-after-median-Virtual-Indexing
O(n) time compleixity, O(n) space complexity
"""
class Solution:
    """
    @param: nums: A list of integers
    @return: nothing
    """
    def wiggleSort(self, nums):
        # write your code here
        if not nums:
            return
        n = len(nums)
        mean = self.get_mean(nums)
        self.three_way_partition(nums, 0, n - 1, mean)
        
        result = [0] * n
        result[::2] = nums[n // 2:]
        result[1::2] = nums[: n // 2]
        nums[:] = result

    def get_mean(self, nums):
        n = len(nums)
        if n % 2 == 1:
            return self.quick_select(nums, 0, n - 1, n // 2 + 1)
        return (self.quick_select(nums, 0, n - 1, n // 2) + self.quick_select(nums, 0, n - 1, n // 2 + 1)) / 2.0
    
    def three_way_partition(self, nums, start, end, mid):
        n = len(nums)
        l = i = 0
        r = n - 1
        while i <= r:
            if nums[i] > mid:
                nums[i], nums[l] = nums[l], nums[i]
                i += 1
                l += 1
            elif nums[i] < mid:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            else:
                i += 1

    def quick_select(self, nums, start, end, k):
        if start >= end:
            return nums[start]

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

        if right - start + 1 >= k:
            return self.quick_select(nums, start, right, k)
        if left - start + 1 <= k:
            return self.quick_select(nums, left, end, k - (left - start))
        return nums[right + 1]