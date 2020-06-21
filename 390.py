"""
390. Find Peak Element II
https://www.lintcode.com/problem/find-peak-element-ii/description?_from=ladder&&fromId=106
"""
import sys
class Solution:
    """
    @param: A: An integer matrix
    @return: The index of the peak
    """
    def findPeakII(self, A):
        # write your code here
        if not A or not A[0]:
            return None
        n = len(A)
        m = len(A[0])
        start_x, end_x = 0, n - 1

        """
        为什么不需要考虑mid + 1或者 -1 越界呢？
        因为start + 1 < end:
        start + 2 <= end
        start mid end
        这个时候循环还可以进入。因此不会越界。
        """
        while start_x + 1 < end_x:
            mid_x = (start_x + end_x) // 2
            col_i = self.find_max_in_col(A, mid_x)
            if A[mid_x][col_i] < A[mid_x + 1][col_i]:
                start_x = mid_x
            elif A[mid_x][col_i] < A[mid_x - 1][col_i]:
                end_x = mid_x
            else:
                return [mid_x, col_i]

        up_col_i = self.find_max_in_col(A, start_x)
        down_col_i = self.find_max_in_col(A, end_x)
        if A[start_x][up_col_i] > A[end_x][down_col_i]:
            return start_x, up_col_i
        return end_x, down_col_i

    def find_max_in_col(self, A, row_index):
        index, max_value = None, -sys.maxsize
        for i, v in enumerate(A[row_index]):
            if v > max_value:
                max_value = v
                index = i
        return index
