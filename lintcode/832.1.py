"""
832. Count Negative Number
https://www.lintcode.com/problem/count-negative-number/description?_from=ladder&&fromId=152
o(n+m)
https://www.jiuzhang.com/solution/count-negative-number/#tag-other
"""
class Solution:
    """
    @param nums: the sorted matrix
    @return: the number of Negative Number
    """
    def countNumber(self, nums):
        # Write your code here
        count = 0
        if not nums:
            return count
        n = len(nums)
        m = len(nums[0])
        i = m - 1
        for row in nums:
            while i >= 0:
                if row[i] < 0:
                    break
                i -= 1
            count += i + 1
        return count