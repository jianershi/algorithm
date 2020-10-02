"""
64. Merge Sorted Array
https://www.lintcode.com/problem/merge-sorted-array/description
o(n) time, o(1) space
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
        i, j = m - 1, n - 1
        t = len(A) - 1
        while i >= 0 and j >= 0:
            if A[i] < B[j]:
                A[t] = B[j]
                j -= 1
            else:
                A[t] = A[i]
                i -= 1
            t -= 1

        while i >= 0:
            A[t] = A[i]
            i -= 1
            t -= 1

        while j >= 0:
            A[t] = B[j]
            j -= 1
            t -= 1
