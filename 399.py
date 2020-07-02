"""
399. Nuts & Bolts Problem
https://www.lintcode.com/problem/nuts-bolts-problem/description
九章算法强化班C7

idea:
pick a pivot in bolts, use the pivot to sort nuts, then using the correstponding nut to sort bolts

"""
"""
class Comparator:
    def cmp(self, a, b)
You can use Compare.cmp(a, b) to compare nuts "a" and bolts "b",
if "a" is bigger than "b", it will return 1, else if they are equal,
it will return 0, else if "a" is smaller than "b", it will return -1.
When "a" is not a nut or "b" is not a bolt, it will return 2, which is not valid.
"""
class Solution:
    # @param nuts: a list of integers
    # @param bolts: a list of integers
    # @param compare: a instance of Comparator
    # @return: nothing
    def sortNutsAndBolts(self, nuts, bolts, compare):
        # write your code here
        

        self.quick_sort(0, len(nuts) - 1, compare, nuts, bolts)

    def quick_sort(self, start, end, compare, nuts, bolts):
        if start >= end:
            return

        index = self.partition(nuts, start, end, bolts[(start + end) // 2], compare, nuts, bolts)
        self.partition(bolts, start, end, nuts[index], compare, nuts, bolts)

        self.quick_sort(start, index - 1, compare, nuts, bolts)
        self.quick_sort(index + 1, end, compare, nuts, bolts)

    def partition(self, nums, start, end, pivot, compare, nuts, bolts):
        left, right = start, end

        #找到bolts的pivot对应的在bolts中的位置。
        for i in range(start, end + 1):
            if compare.cmp(nums[i], pivot) == 0 or compare.cmp(pivot, nums[i]) == 0:
                nums[left], nums[i] = nums[i], nums[left] #先扔到开始位置保存
                left += 1 #然后从start +1 后面先partition
                break

        while left <= right:
            while left <= right and (compare.cmp(nums[left], pivot) == -1 or compare.cmp(pivot, nums[left]) == 1):
                left += 1
            while left <= right and (compare.cmp(nums[right], pivot) == 1 or compare.cmp(pivot, nums[right]) == -1):
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        nums[start], nums[right] = nums[right], nums[start] #然后再把pivot放回原来的位置
        #要是和left换的话比pivot大的值就换到最左边去了。所以只能和right换
        return right

