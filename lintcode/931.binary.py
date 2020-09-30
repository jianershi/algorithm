"""
931. Median of K Sorted Arrays
https://www.lintcode.com/problem/median-of-k-sorted-arrays/description
"""
import sys
class Solution:
    """
    @param nums: the given k sorted arrays
    @return: the median of the given k sorted arrays
    """
    def findMedian(self, nums):
        # if not nums:
        #     return 0
        total_numbers = self.count_how_many_numbers_total(nums)
        if total_numbers == 0:
            return 0
        if total_numbers % 2 == 1:
            return self.binary_search(nums, total_numbers // 2 + 1) * 1.0
        # return (self.binary_search(nums, total_numbers // 2) + self.binary_search(nums, total_numbers // 2 + 1)) / 2.0
        print ("total number: %d, kth = %d" % (total_numbers, total_numbers // 2 + 1))
        return (self.binary_search(nums, total_numbers // 2 + 1))

    def count_how_many_numbers_total(self, nums):
        length_list = [len(x) for x in nums]
        return sum(length_list)

    def binary_search(self, nums, k):
        smallest_elements = [x[0] if len(x) > 0 else sys.maxsize for x in nums]
        biggest_elements = [x[-1] if len(x) > 0 else -sys.maxsize for x in nums]
        start, end = min(smallest_elements), max(biggest_elements)

        while start + 1 < end:
            mid = (start + end) // 2
            print ("mid = %d" % mid)
            print ("start = %d, mid = %d, end = %d, k = %d" % (start, mid, end, k))
            if self.count_elements_before_in_all_arrays(nums, mid) < k:
                start = mid
            else:
                end = mid
        print ("start = %d, mid = %d, end = %d, k = %d" % (start, mid, end, k))
        if self.count_elements_before_in_all_arrays(nums, start) >= k:
            return start
        if self.count_elements_before_in_all_arrays(nums, end) >= k:
            return end
        return -1

    def count_elements_before_in_all_arrays(self, array_of_lists, target):
        count = 0
        for arr in array_of_lists:
            count += self.count_elements_before_in_an_array(arr, target)
        print (array_of_lists, target, count)
        return count

    """
    find how many numbers >= target
    """
    def count_elements_before_in_an_array(self, nums, target):
        if len(nums) == 0:
            return 0
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            else:
                end = mid
        if nums[start] > target:
            return start
        if nums[end] > target:
            return end
        return end + 1


s = Solution()
# nums = [[1],[],[2],[3],[3]]
nums = [[1,3],[2147483646,2147483647]]
print (s.findMedian(nums))
