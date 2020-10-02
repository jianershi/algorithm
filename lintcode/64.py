"""
64. Merge Sorted Array
https://www.lintcode.com/problem/merge-sorted-array/description
o(n) time, o(n) space
"""
class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        res = []
        i, j = 0, 0
        while i < m and j < n:
            if A[i] < B[j]:
                res.append(A[i])
                i += 1
            else:
                res.append(B[j])
                j += 1

        while i < m:
            res.append(A[i])
            i += 1

        while j < n:
            res.append(B[j])
            j += 1

        A[:] = list(res)