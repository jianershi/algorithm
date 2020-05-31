"""
0.......i.....j
if i+++ j == 0
0---j = 0 --- i
O(n)
"""
class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        prefix_sum = 0
        prefix_sum_to_index = {0: -1}

        for i, number in enumerate(nums):
            prefix_sum += number
            if prefix_sum in prefix_sum_to_index:
                return (prefix_sum_to_index[prefix_sum] + 1, i)
            prefix_sum_to_index[prefix_sum] = i
        return (-1, -1)

"""
第二个方法是错的。
本来想着先排序。然后二分查找，2跟指针。但这个是错误的。

"""
# class Solution:
#     """
#     @param nums: A list of integers
#     @return: A list of integers includes the index of the first number and the index of the last number
#     """
#     def subarraySum(self, nums):
#         if not nums:
#             return -1, -1
#         nums.sort()
#         # print (nums)
#         first_positive_index = self.binary_search(nums, 0)
#         # print (first_positive_index)
#         left, right = first_positive_index, first_positive_index
#         # print (left, right)
#         sums = nums[first_positive_index]
#         while left >= 0 and right < len(nums):
#             if sums > 0:
#                 left -= 1
#                 sums += nums[left]
#                 # print(left, sums)
#                 continue
#             if sums < 0:
#                 right += 1
#                 sums += nums[right]
#                 # print (right, sums)
#                 continue
#             # print (left, right, sums)
#             return [left, right]
#         return -1, -1


#     def binary_search(self, nums, target):
#         # if not nums:
#             # return -1
#         start, end = 0, len(nums) - 1
#         while start + 1 < end:
#             mid = (start + end) // 2
#             if nums[mid] < target:
#                 start = mid
#             else:
#                 end = mid
#         if nums[start] >= target:
#             return start
#         if nums[end] >= target:
#             return end
#         return -1
