"""
404. Subarray Sum II

https://www.lintcode.com/problem/subarray-sum-ii/description

prefix sum definition including itself
"""
class Solution:
    """
    @param A: An integer array
    @param start: An integer
    @param end: An integer
    @return: the number of possible answer
    """
    def subarraySumII(self, A, start, end):
        # write your code here
        n = len(A)
        prefix_sum = [0] * n
        l = r = 0
        count = 0
        for j in range(n):
            if j == 0:
                prefix_sum[j] = A[0]
            else:
                prefix_sum[j] = prefix_sum[j - 1] + A[j]
            """
            .....xxxoooooxxxxx..j
                    l    r
            """
            while l <= j and prefix_sum[j] - prefix_sum[l - 1] > end:
                l += 1

            while r <= j and prefix_sum[j] - prefix_sum[r - 1] >= start:
                r += 1

            count += r - l
        return count

