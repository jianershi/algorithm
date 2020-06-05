class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers(self, A):
        # write your code here
        if not A:
            return

        self.quick_sort(A, 0, len(A) - 1)
        # temp = [0] * len(A)
        # self.merge_sort(A, 0, len(A) - 1, temp)

    def quick_sort(self, nums, start, end):
        if start >= end:
            return
        left = start
        right = end
        pivot = (nums[left] + nums[right]) // 2
        while left <= right:
            while nums[left] < pivot:
                left += 1
            while nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        self.quick_sort(nums, start, right)
        self.quick_sort(nums, left, end)

    # def merge_sort(self, nums, start, end, temp):
    #     if start >= end:
    #         return

    #     self.merge_sort(nums, start, (start + end) // 2, temp)
    #     self.merge_sort(nums, (start + end) // 2 + 1, end, temp)
    #     self.merge_sort_merge(nums, start, end, temp)
    # def merge_sort_merge(self, nums, start, end, temp):
    #     mid = (start + end) // 2
    #     index = start
    #     left = start
    #     right = mid + 1
    #     while left <= mid and right <= end:
    #         if nums[left] < nums[right]:
    #             temp[index] = nums[left]
    #             left += 1
    #         else:
    #             temp[index] = nums[right]
    #             right += 1
    #         index += 1

    #     while left <= mid:
    #         temp[index] = nums[left]
    #         left += 1
    #         index += 1
    #     while right <= end:
    #         temp[index] = nums[right]
    #         right += 1
    #         index += 1
    #     for index in range(start, end + 1):
    #         nums[index] = temp[index]
